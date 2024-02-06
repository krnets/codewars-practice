from functools import reduce

bin = "01"
oct = "01234567"
dec = "0123456789"
hex = "0123456789abcdef"
allow = "abcdefghijklmnopqrstuvwxyz"
allup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphanum = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def convert(input, source, target):
    base_s, base_t = len(source), len(target)
    num = reduce(lambda x, c: x * base_s + source.index(c), input, 0)
    ans = ""
    while num:
        ans = target[num % base_t] + ans
        num //= base_t
    return ans if ans else target[0]
