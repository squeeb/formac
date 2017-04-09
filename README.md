# Formac
Format any MAC address for use with multiple vendor devices that use different
MAC formatting

Cisco use `aabb.cc11.2233`, Dell DNOS6 uses `aa-bb-cc-11-22-33`, FTOS and DNOS9
use `aa:bb:cc:11:22:33`.

This tool is just a handy way to take any of these formats and print out any
other format.

### Usage:
```
usage: formac.py [-h] [-U] [-g {2,4}] [-s {:,.,-,none}] nn:nn:nn:nn:nn:nn

Format MAC addresses

positional arguments:
  nn:nn:nn:nn:nn:nn     a MAC address in any format

optional arguments:
  -h, --help            show this help message and exit
  -U, --upcase          Make output uppercase
  -g {2,4}, --group {2,4}
                        Byte grouping size
  -s {:,.,-,none}, --seperator {:,.,-,none}
                        seperator character
```
