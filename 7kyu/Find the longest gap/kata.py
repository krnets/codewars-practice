import re

# def gap(num):
#     arr = re.findall(r"10+(?=1)", f"{num:b}")
#     return max(map(len, arr)) - 1 if arr else 0


# def gap(num):
#     arr = re.findall(r"(?<=1)0+(?=1)", f"{num:b}")
#     return max(map(len, arr), default=0)


# def gap(num):
#     arr = re.findall(r"0+(?=1)", f"{num:b}")
#     return max(map(len, arr), default=0)


def gap(num):
    arr = re.findall(r"0+(?=1)", bin(num))
    return max(map(len, arr), default=0)
