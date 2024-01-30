from math import prod


def persistence(n):
    ans = 0
    while n > 9:
        n = prod(map(int, str(n)))
        ans += 1
    return ans
