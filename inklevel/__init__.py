from collections import namedtuple

import inklevel._cbindings
from inklevel._constants import CartridgeType, ReturnValue, Port

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def get_ink_level(port, device_file, portnumber):
    return_value, data = inklevel._cbindings.get_ink_level_c(port.value, device_file, portnumber)

    if return_value != ReturnValue.OK.value:
        raise InklevelError(ReturnValue(return_value))

    model = data.model.decode()
    parsed_levels = []
    for level in data.levels:
        cartridge_type = CartridgeType(level[0])
        if cartridge_type != CartridgeType.NOT_PRESENT:
            parsed_levels.append((cartridge_type, level[1]))

    return Inklevel(model, parsed_levels)


def get_usb_ink_level(portnumber):
    return get_ink_level(Port.USB, None, portnumber)


def get_parport_ink_level(portnumber):
    return get_ink_level(Port.PARPORT, None, portnumber)


def get_version_string():
    return inklevel._cbindings.get_version_string_c().decode()


class Inklevel(namedtuple('Inklevel', 'model levels')):

    pass


class InklevelError(Exception):

    def __init__(self, return_value):
        self.return_value = return_value

    def __str__(self):
        return 'Error {}: {}'.format(self.return_value.value, self.return_value.name)
