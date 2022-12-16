def calc(x):
    total1 = [int(t) for c in x for t in str(ord(c))]
    total2 = [1 if t == 7 else t for t in total1]
    return sum(total1) - sum(total2)


q = calc("ABC")  # 6
q
q = calc("abcdef")  # 6
q
q = calc("ifkhchlhfd")  # 6
q
q = calc("aaaaaddddr")  # 30
q
q = calc("jfmgklf8hglbe")  # 6
q
q = calc("jaam")  # 12
q
