# import re


# def calculate(s):
#     arr = re.findall(r"\d+|[a-z]+", s)
#     res = int(arr[0])

#     for i in range(1, len(arr) - 1, 2):
#         if arr[i] == "plus":
#             res += int(arr[i + 1])
#         elif arr[i] == "minus":
#             res -= int(arr[i + 1])

#     return str(res)


def calculate(s):
    s = s.replace("plus", " ")
    s = s.replace("minus", " -")
    return str(sum(map(int, s.split())))
