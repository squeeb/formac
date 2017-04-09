#!/usr/bin/env python

import sys
import string
import argparse

parser = argparse.ArgumentParser(description='Format MAC addresses')
parser.add_argument('mac_address_raw', metavar='nn:nn:nn:nn:nn:nn', type=str, nargs=1,
        help='a MAC address in any format')
parser.add_argument('-U', '--upcase', help='Make output uppercase', action='store_true')
parser.add_argument('-g', '--group', type=int, choices=[2,4], help='Byte grouping size')
parser.add_argument('-s', '--seperator', type=str, choices=[':','.','-','none'], help='seperator character')

args = parser.parse_args()
mac_address_raw = args.mac_address_raw[0]
mac_address = mac_address_raw.translate(None, '.:-_')

def is_hex(s):
    return all(c in string.hexdigits for c in s)

def is_mac_address(s):
    if is_hex(s) and (len(s) == 12):
        return True
    else:
        return False

def is_upcase():
    if args.upcase:
        return True
    else:
        return False

def interval():
    if args.group:
        return args.group
    else:
        return 2

def seperator():
    if args.seperator:
        if args.seperator == 'None':
            return ''
        else:
            return args.seperator
    else:
        return ':'

def generate_mac(mac_address, seperator, interval):
    if is_upcase():
        mac_address = mac_address.upper()

    return seperator.join(mac_address[i:i+interval]
            for i in range(0, len(mac_address), interval))

if is_mac_address(mac_address):
    print generate_mac(mac_address, seperator(), interval())
else:
    print "%s is not a valid MAC address" % mac_address_raw
    exit(1)
