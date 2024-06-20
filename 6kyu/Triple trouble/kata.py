import re

# def triple_double(num1, num2):
#     triple = re.findall(r"(.)\1\1", str(num1))
#     return triple[0] in re.findall(r"(.)\1", str(num2)) if triple else 0


def triple_double(num1, num2):
    return bool(re.search(r"(\d)\1\1.* .*\1\1", f"{num1} {num2}"))
