import re

def case_id(c_str):
    cases = [("kebab", r"[a-z]+(-[a-z]+)+"),
             ("snake", r"[a-z]+(_[a-z]+)+"),
             ("camel", r"[a-z]+([A-Z][a-z]+)+")]
    for convention, pattern in cases:
        if re.fullmatch(pattern, c_str):
            return convention
    return "none"
