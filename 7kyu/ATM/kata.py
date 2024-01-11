def solve(n):
    if n % 10 != 0:
        return -1
    banknotes = [10, 20, 50, 100, 200, 500]
    ans = 0
    for note in reversed(banknotes):
        if n >= note:
            x = n // note
            ans += x
            n -= note * x

    return ans
