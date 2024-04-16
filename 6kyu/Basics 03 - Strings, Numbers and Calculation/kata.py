import re

# def calculate_string(st):
#     return str(round(eval("".join(re.findall(r"[+\-*/.\d]+", st)))))


def calculate_string(st):
    return str(round(eval(re.sub(r"[^+\-*/.\d]", "", st))))
