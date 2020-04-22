# 6kyu - Regexp Basics - is it IPv4 address?

""" Implement ipv4_address, which should return true if given object is an IPv4 address - 
four numbers (0-255) separated by dots.

It should only accept addresses in canonical representation, so no leading 0s, spaces etc. """

import re

# def ipv4_address(address):
#     ip = '(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
#     return bool(re.fullmatch('^(' + ip + '\.){3}' + ip, address))

def ipv4_address(address):
    return bool(re.match('((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(?!$)|$)){4}\Z', address))


q = ipv4_address(""), False
q
q = ipv4_address("127.0.0.1"), True
q
q = ipv4_address("0.0.0.0"), True
q
q = ipv4_address("255.255.255.255"), True
q
q = ipv4_address("10.20.30.40"), True
q
q = ipv4_address("10.256.30.40"), False
q
q = ipv4_address("10.20.030.40"), False
q
q = ipv4_address("127.0.1"), False
q
q = ipv4_address("127.0.0.0.1"), False
q
q = ipv4_address("..255.255"), False
q
q = ipv4_address("127.0.0.1\n"), False
q
q = ipv4_address("\n127.0.0.1"), False
q
q = ipv4_address(" 127.0.0.1"), False
q
q = ipv4_address("127.0.0.1 "), False
q
q = ipv4_address(" 127.0.0.1 "), False
q
