def pattern(n):
    return "\n".join(str(i) * i for i in range(1, n + 1))


q = pattern(1)  # 1
q
q = pattern(2)  # 1\n22
q
q = pattern(5)  # 1\n22\n333\n4444\n55555
q
q = pattern(0)  # ''
q
q = pattern(-25)  #''
q
