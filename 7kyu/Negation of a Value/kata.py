# def negation_value(s, val):
#     return not bool(val) if len(s) & 1 else bool(val)

def negation_value(s, val):
    for _ in s:
        val = not val
    return val