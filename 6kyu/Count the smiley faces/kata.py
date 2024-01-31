import re

# def count_smileys(arr):
#     return sum(bool(re.findall(r"^[:;][-~]?[D)]$", x)) for x in arr)


def count_smileys(arr):
    return sum(bool(re.match(r"[:;][-~]?[D)]", x)) for x in arr)
