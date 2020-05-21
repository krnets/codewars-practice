# 8kyu - Parse float

""" Write function parseFloat which takes a string and returns a number or None if conversion is not possible. """


def parse_float(string):
    try:
        return float(string)
    except:
        return


q = parse_float("1.0"), 1.0
q
q = parse_float("234.0234"), 234.0234
q
q = parse_float("a"), None
q
