# def unused_digits(*numbers):
#     digits = [chr(i + ord("0")) for i in range(10)]
#     seen = set("".join(map(str, numbers)))
#     return "".join(d for d in digits if d not in seen)

from string import digits
from itertools import chain


def unused_digits(*numbers):
    # return "".join(sorted(set(digits) - set("".join(map(str, numbers)))))
    return "".join(sorted(set(digits) - set(chain.from_iterable(map(str, numbers)))))
