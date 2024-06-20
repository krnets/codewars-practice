import re


# def valid_number(n):
#     return bool(re.fullmatch(r"[+-]?\d*\.\d\d", str(n)))


def valid_number(n):
    return bool(re.fullmatch(r"""
        [+-]?   # optional +/- sign
        \d*     # optional digits
        \.      # decimal point
        \d\d    # two digits
        """, str(n), re.VERBOSE))