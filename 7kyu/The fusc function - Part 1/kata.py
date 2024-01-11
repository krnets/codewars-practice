def fusc(n):
    if n < 2:
        return n
    if n % 2 == 0:
        return fusc(n // 2)
    return fusc(n // 2) + fusc(n // 2 + 1)
