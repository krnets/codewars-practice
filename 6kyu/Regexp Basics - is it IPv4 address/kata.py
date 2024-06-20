import re


def ipv4_address(address):
    pattern = re.compile("(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}")
    return bool(re.fullmatch(pattern, address))
