from math import ceil, log

def bin_str(s):
    n = int(s, 2)
    ans = 0
    while n > 0:
        n = ~n & (1 << (ceil(log(n, 2)))) - 1
        ans += 1
    return ans
