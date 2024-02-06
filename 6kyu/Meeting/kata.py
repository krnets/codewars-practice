# def meeting(s):
#     names = [(name.split(":")[::-1]) for name in s.upper().split(";")]
#     return "".join("({}, {})".format(*name[:2]) for name in sorted(names))


def meeting(s):
    return "".join(sorted("({1}, {0})".format(*name.split(":")) for name in s.upper().split(";")))
