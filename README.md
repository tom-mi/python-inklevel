# python-inklevel

Python wrapper for [libinklevel](http://libinklevel.sourceforge.net/).

## Prerequisites

Install [libinklevel](http://libinklevel.sourceforge.net/), e.g. on Debian:

    apt-get install libinklevel

## Usage

    import inklevel

    # libinklevel version
    print(inklevel.get_version_string())

    # Get data from /dev/usb/lp0:
    data = inklevel.get_usb_ink_level(0)

    for cartridge, value in data.levels:
        print('{}: {}'.format(cartridge.description, value))

    # Get data from /dev/parport2
    data = inklevel.get_parport_ink_level(2)

The functions `get_usb_ink_level` and `get_parport_ink_level` are convenience functions using the original libinklevel interface. You can also use that:

    data = inklevel.get_ink_level(inklevel.Port.USB, None, 0)
    data = inklevel.get_ink_level(inklevel.Port.CUSTOM_USB, '/dev/usb/lp0', None)

See [libinklevel](http://libinklevel.sourceforge.net/) and [ink](http://ink.sourceforge.net/) for details.

## License

This software is licensed under GPLv2.
