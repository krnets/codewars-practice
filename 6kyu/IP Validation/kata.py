# def is_valid_IP(strng):
#     octets = strng.split(".")
#     return len(octets) == 4 and all(x.isnumeric() and 0 <= int(x) <= 255 and not (x[0] == "0" and len(x) > 1) for x in octets)

# from ipaddress import ip_address


# def is_valid_IP(strng):
#     try:
#         return bool(ip_address(strng))
#     except:
#         return False

import re

def is_valid_IP(strng):
    return bool(re.match(r"(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}", strng))
