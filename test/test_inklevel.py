import inklevel

from inklevel import _cbindings
from inklevel._constants import CartridgeType, ReturnValue, Port

import pytest


@pytest.fixture
def mocked_ink_level(monkeypatch):
    ink_level = _cbindings.INK_LEVEL()
    monkeypatch.setattr('inklevel._cbindings.get_ink_level_c', lambda _1, _2, _3: (0, ink_level))
    return ink_level


def test_cartridge_descriptions():
    for cartridge in CartridgeType:
        assert len(cartridge.description) > 0


def test_parsing_of_single_cartridge(mocked_ink_level):
    mocked_ink_level.model = b'Printing Press 2.0'
    mocked_ink_level.status = 1
    mocked_ink_level.levels[0][0] = 1
    mocked_ink_level.levels[0][1] = 42

    result = inklevel.get_ink_level(Port.PARPORT, None, 0)
    assert result.model == 'Printing Press 2.0'
    assert result.levels == [(CartridgeType.BLACK, 42)]


def test_parsing_of_multiple_cartridges(mocked_ink_level):
    mocked_ink_level.levels[0][0] = 1
    mocked_ink_level.levels[0][1] = 42
    mocked_ink_level.levels[1][0] = 2
    mocked_ink_level.levels[1][1] = 17

    result = inklevel.get_ink_level(Port.PARPORT, None, 0)
    assert result.levels == [
        (CartridgeType.BLACK, 42),
        (CartridgeType.COLOR, 17),
    ]


def test_passing_of_argements(monkeypatch):
    test_port = Port.PARPORT
    test_device_file = '/dev/my/printer'
    test_portnumber = 42
    ink_level = _cbindings.INK_LEVEL()

    def mock_get_ink_level(port, device_file, portnumber):
        assert port == test_port.value
        assert device_file == test_device_file
        assert portnumber == test_portnumber
        return (0, ink_level)

    monkeypatch.setattr('inklevel._cbindings.get_ink_level_c', mock_get_ink_level)

    inklevel.get_ink_level(test_port, test_device_file, test_portnumber)


def test_get_usb_ink_level(mocker):
    mock_return = 'The inkpot is nearly empty.'

    with mocker.patch('inklevel.get_ink_level', return_value=mock_return):
        result = inklevel.get_usb_ink_level(42)

    assert result == mock_return
    inklevel.get_ink_level.assert_called_once_with(Port.USB, None, 42)


def test_get_parport_ink_level(mocker):
    mock_return = 'The inkpot is nearly empty.'

    with mocker.patch('inklevel.get_ink_level', return_value=mock_return):
        result = inklevel.get_parport_ink_level(42)

    assert result == mock_return
    inklevel.get_ink_level.assert_called_once_with(Port.PARPORT, None, 42)


def test_error(monkeypatch):
    ink_level = _cbindings.INK_LEVEL()
    ink_level.status = 0

    monkeypatch.setattr('inklevel._cbindings.get_ink_level_c', lambda _1, _2, _3: (-1, ink_level))

    with pytest.raises(inklevel.InklevelError) as excinfo:
        inklevel.get_ink_level(Port.PARPORT, None, 0)
    assert '-1' in str(excinfo.value)


def test_library_error():
    # FIXME: Add another test returning success. This requires mocking a printer.
    with pytest.raises(inklevel.InklevelError) as excinfo:
        inklevel.get_ink_level(Port.PARPORT, None, 42)
    assert excinfo.value.return_value == ReturnValue.DEV_PARPORT_INACCESSIBLE


def test_library_version_string():
    assert u'libinklevel' in inklevel.get_version_string()
