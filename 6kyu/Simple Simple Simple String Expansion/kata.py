def string_expansion(s):
    n, res = 1, ""
    for c in s:
        if c.isalpha():  res += c * n
        else:            n = int(c)
    return res