#formac
Format any MAC address for use with multiple vendor devices that use different
MAC formatting

Cisco use `aabb.cc11.2233`, Dell DNOS6 uses `aa-bb-cc-11-22-33`, FTOS and DNOS9
use `aa:bb:cc:11:22:33`.

This tool is just a handy way to take any of these formats and print out any
other format.

###usage:
```
./formac.py aabbcc112233
./formac.py aa:bb:cc:11:22:33
./formac.py aa-bb-cc-11-22-33
./formac.py aabb.cc11.2233
```
