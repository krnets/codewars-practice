import re
from textwrap import wrap

# def sort_by_num(s):
#     splits = re.findall(r"[a-z]\d", s)
#     return "".join(sorted(splits, key=lambda x: x[1]))


def sort_by_num(s):
    return "".join(sorted(wrap(s, 2), key=lambda x: x[1]))
