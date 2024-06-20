import re


def find_e(s):
    if not s:
        return s
    return str(len(m)) if (m := re.findall(r"[Ee]", s)) else 'There is no "e".'
