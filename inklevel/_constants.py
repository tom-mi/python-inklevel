'''Autogenerated class containing constants from `inklevel.h` and `ink.c`'''

from enum import Enum


_MODEL_NAME_LENGTH = 100
_MAX_CARTRIDGE_TYPES = 40


_RESPONSE_INVALID = 0
_RESPONSE_VALID = 1


class Port(Enum):

    PARPORT = 1
    USB = 2
    CUSTOM_PARPORT = 3
    CUSTOM_USB = 4
    BJNP = 5
    CUSTOM_BJNP = 6


class ReturnValue(Enum):

    OK = 0
    ERROR = -1
    DEV_PARPORT_INACCESSIBLE = -2
    DEV_LP_INACCESSIBLE = -3
    COULD_NOT_GET_DEVICE_ID = -4
    DEV_USB_LP_INACCESSIBLE = -5
    UNKNOWN_PORT_SPECIFIED = -6
    NO_PRINTER_FOUND = -7
    NO_DEVICE_CLASS_FOUND = -8
    NO_CMD_TAG_FOUND = -9
    PRINTER_NOT_SUPPORTED = -10
    NO_INK_LEVEL_FOUND = -11
    COULD_NOT_WRITE_TO_PRINTER = -12
    COULD_NOT_READ_FROM_PRINTER = -13
    COULD_NOT_PARSE_RESPONSE_FROM_PRINTER = -14
    COULD_NOT_GET_CREDIT = -15
    DEV_CUSTOM_USB_INACCESSIBLE = -16
    BJNP_URI_INVALID = -17
    BJNP_INVALID_HOSTNAME = -18


class CartridgeType(Enum):

    NOT_PRESENT = 0
    BLACK = 1
    COLOR = 2
    PHOTO = 3
    CYAN = 4
    MAGENTA = 5
    YELLOW = 6
    PHOTOBLACK = 7
    PHOTOCYAN = 8
    PHOTOMAGENTA = 9
    PHOTOYELLOW = 10
    RED = 11
    GREEN = 12
    BLUE = 13
    LIGHTBLACK = 14
    LIGHTCYAN = 15
    LIGHTMAGENTA = 16
    LIGHTLIGHTBLACK = 17
    MATTEBLACK = 18
    GLOSSOPTIMIZER = 19
    UNKNOWN = 20
    KCM = 21
    GGK = 22
    KCMY = 23
    LCLM = 24
    YM = 25
    CK = 26
    LGPK = 27
    LG = 28
    G = 29
    PG = 30
    WHITE = 31

    @property
    def description(self):
        return _CARTRIDGE_DESCRIPTIONS[self.value]


_CARTRIDGE_DESCRIPTIONS = [
    'Not present',
    'Black',
    'Color',
    'Photo',
    'Cyan',
    'Magenta',
    'Yellow',
    'Photoblack',
    'Photocyan',
    'Photomagenta',
    'Photoyellow',
    'Red',
    'Green',
    'Blue',
    'Light Black',
    'Light Cyan',
    'Light Magenta',
    'Light Light Black',
    'Matte Black',
    'Gloss Optimizer',
    'Unknown',
    'Light Cyan, Light Magenta, Photoblack',
    '2x Grey and Black',
    'Black, Cyan, Magenta, Yellow',
    'Photocyan and Photomagenta',
    'Yellow and Magenta',
    'Cyan and Black',
    'Light Grey and Photoblack',
    'Light Grey',
    'Medium Grey',
    'Photogrey',
    'White',
]
