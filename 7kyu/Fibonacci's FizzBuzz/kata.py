# def fibs_fizz_buzz(n):
#     a, b = 1, 1
#     res = [a]

#     for _ in range(n - 1):
#         a, b = b, a + b
#         s = ""
#         if a % 3 == 0: s += "Fizz"
#         if a % 5 == 0: s += "Buzz"
#         res.append(s if s else a)

#     return res


def fibs_fizz_buzz(n):
    a, b = 0, 1
    res = []

    for _ in range(n):
        s = "Fizz" * (b % 3 == 0) + "Buzz" * (b % 5 == 0)
        res.append(s if s else b)
        a, b = b, a + b

    return res
