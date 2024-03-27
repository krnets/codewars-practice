def total_bill(s):
    n = len(s.replace(" ", ""))
    q, r = divmod(n, 5)
    return (4 * q + r) * 2
