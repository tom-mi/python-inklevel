from ctypes import byref, cdll, c_ushort, c_char_p, create_string_buffer, Structure

from inklevel._constants import (
    _MODEL_NAME_LENGTH, _MAX_CARTRIDGE_TYPES,
)

lib = cdll.LoadLibrary('libinklevel.so.5')
lib.get_version_string.restype = c_char_p


class INK_LEVEL(Structure):
    _fields_ = [
        ('model', type(create_string_buffer(_MODEL_NAME_LENGTH))),
        ('status', c_ushort),
        ('levels', (c_ushort * 2) * _MAX_CARTRIDGE_TYPES),
    ]


def get_ink_level_c(port, device_file, portnumber):
    levels = INK_LEVEL()
    return_value = lib.get_ink_level(port, device_file, portnumber, byref(levels))
    return (return_value, levels)


def get_version_string_c():
    return lib.get_version_string()
