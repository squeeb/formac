#!/usr/bin/env python

import sys
import string

try:
    mac_address_raw = sys.argv[1]
except IndexError:
    print "Usage: %s <mac address>" % sys.argv[0]
    exit(1)

try:
    generate_type = sys.argv[2]
except IndexError:
    generate_type = all

mac_address = mac_address_raw.translate(None, '.:-_')

def is_hex(s):
    return all(c in string.hexdigits for c in s)

def is_mac_address(s):
    if is_hex(s) and (len(s) == 12):
        return True
    else:
        return False

def generate_mac(mac_address, delimiter, interval):
    return delimiter.join(mac_address[i:i+interval]
            for i in range(0, len(mac_address), interval))

if is_mac_address(mac_address):
    print generate_mac(mac_address, ':', 2)
    print generate_mac(mac_address, '.', 4)
    print generate_mac(mac_address, '-', 2)
else:
    print "%s is not a valid MAC address" % mac_address_raw
    exit(1)
