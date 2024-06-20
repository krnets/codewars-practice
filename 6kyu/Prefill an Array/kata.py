import re

def prefill(n, v=0):
    if bool(re.findall(r'\D+', str(n))):
        raise TypeError(f"{n} is invalid")
    return [v] * int(n) if n else []