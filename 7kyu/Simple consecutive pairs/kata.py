def pairs(ar):
    return sum(abs(x - y) == 1 for (x, y) in zip(ar[::2], ar[1::2]))


q = pairs([1, 2, 5, 8, -4, -3, 7, 6, 5])  # 3
q
q = pairs([21, 20, 22, 40, 39, -56, 30, -55, 95, 94])  # 2
q
q = pairs([81, 44, 80, 26, 12, 27, -34, 37, -35])  # 0
q
q = pairs([-55, -56, -7, -6, 56, 55, 63, 62])  # 4
q
q = pairs([73, 72, 8, 9, 73, 72])  # 3
q
