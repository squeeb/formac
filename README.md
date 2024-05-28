# Formac
Format any MAC address for use with multiple vendor devices that use different
MAC formatting

Cisco use `aabb.cc11.2233`, Dell DNOS6 uses `aa-bb-cc-11-22-33`, FTOS and DNOS9
use `aa:bb:cc:11:22:33`.

This tool is just a handy way to take any of these formats and print out any
other format.

### Usage:
```
usage: formac.py [-h] [-U] [-l] [-g {2,4}] [-s {:,.,-,none}] [--cisco] [-o] nn:nn:nn:nn:nn:nn

Format MAC addresses

positional arguments:
  nn:nn:nn:nn:nn:nn     a MAC address in any format

options:
  -h, --help            show this help message and exit
  -U, --upcase          Make output uppercase
  -l, --lowercase       Make output lowercase
  -g {2,4}, --group {2,4}
                        Byte grouping size
  -s {:,.,-,none}, --seperator {:,.,-,none}
                        seperator character
  --cisco               Shortcut to --group 4 --seperator .
  -o, --ouilookup       Do an OUI lookup against Wireshark's public OUI database
```
