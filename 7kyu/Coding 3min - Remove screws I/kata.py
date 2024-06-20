# def sc(s):
#     return 5 * (s.count("+-") + s.count("-+")) + 2 * len(s) - 1

import re

def sc(s):
    return 5 * len(re.findall(r"\+(?=-)|-(?=\+)", s)) + 2 * len(s) - 1
