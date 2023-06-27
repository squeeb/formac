#!/usr/bin/env python3

import sys
import string
import argparse
import requests
import re

parser = argparse.ArgumentParser(description='Format MAC addresses')
parser.add_argument('mac_address_raw', metavar='nn:nn:nn:nn:nn:nn', type=str, nargs=1,
        help='a MAC address in any format')
parser.add_argument('-U', '--upcase', help='Make output uppercase', action='store_true')
parser.add_argument('-l', '--lowercase', help='Make output lowercase', action='store_true')
parser.add_argument('-g', '--group', type=int, choices=[2,4], help='Byte grouping size')
parser.add_argument('-s', '--seperator', type=str, choices=[':','.','-','none'], help='seperator character')
parser.add_argument('--cisco', dest='cisco', action='store_true', help='Shortcut to --group 4 --seperator .')
parser.add_argument('-o', '--ouilookup', help="Do an OUI lookup against Wireshark's public OUI database", action='store_true')
parser.set_defaults(cisco=False)

args = parser.parse_args()
mac_address_raw = args.mac_address_raw[0]
mac_address = mac_address_raw.translate(
    mac_address_raw.maketrans(".:-_", ".:-_", ".:-_")
)

if args.cisco:
    args.group = 4
    args.seperator = "."
    args.lowercase = True


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


def is_lowercase():
    if args.lowercase:
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
        if args.seperator == "none":
            return ""
        else:
            return args.seperator
    else:
        return ":"


def generate_mac(mac_address, seperator, interval):
    if is_upcase():
        mac_address = mac_address.upper()
    elif is_lowercase():
        mac_address = mac_address.lower()

    return seperator.join(
        mac_address[i : i + interval] for i in range(0, len(mac_address), interval)
    )


def oui_lookup(mac_address):
    mac_addr = generate_mac(mac_address, ':', 2)
    oui = ':'.join(mac_addr.split(':')[0:3]).upper().strip()
    r = requests.get('https://gitlab.com/wireshark/wireshark/-/raw/master/manuf')
    if r.status_code == 200:
        matches = re.findall("%s.*" % oui, r.text, re.MULTILINE)
        if matches:
            ret = matches
        else:
            ret = False
    else:
        ret = False

    return ret

if is_mac_address(mac_address):
    print(generate_mac(mac_address, seperator(), interval()))
    if args.ouilookup:
        matches = oui_lookup(mac_address)

        if matches:
            for match in matches:
                print(match)
        else:
            print('No OUI matches found')
else:
    print("%s is not a valid MAC address" % mac_address_raw)
    exit(1)
