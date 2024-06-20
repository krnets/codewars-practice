def validate(n):
    digits = []
    for i, x in enumerate(map(int, reversed(str(n)))):
        if i & 1:
            x *= 2
            digits.append(x - 9 if x > 9 else x)
        else:
            digits.append(x)
    return sum(digits) % 10 == 0
