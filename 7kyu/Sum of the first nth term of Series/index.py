# 7kyu - Sum of the first nth term of Series

""" Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

Rules:

    You need to round the answer to 2 decimal places and return it as String.
    If the given value is 0 then it should return 0.00
    You will only be given Natural Numbers as arguments.

Examples:

SeriesSum(1) => 1 = "1.00"
SeriesSum(2) => 1 + 1/4 = "1.25"
SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57" """

# def series_sum(n):
#     res = []
#     i = 1
#     while(len(res) != n):
#         res.append(1 / i)
#         i += 3
#     return '{0:.2f}'.format(sum(res), 2)

# def series_sum(n):
#     s = 0
#     for i in range(n):
#         s += 1 / (1 + 3 * i)
#     return '{0:.2f}'.format(s)

# def series_sum(n):
#     return '{:.2f}'.format(sum(1 / (3 * i + 1) for i in range(n)))


# def series_sum(n):
#     m = 1
#     ans = 0

#     while n:
#         ans += 1 / m
#         m += 3
#         n -= 1

#     return f"{ans:.2f}"


# def series_sum(n, sum=0):
#     return series_sum(n - 1, sum + 1 / (3 * n - 2)) if n else f"{sum:.2f}"


# def series_sum(n):
#     return "{:.2f}".format(sum(1.0 / (i * 3 + 1) for i in range(n)))


def series_sum(n):
    return "%.2f" % sum(1.0 / (i * 3 + 1) for i in range(n))


q = series_sum(1)  # "1.00"
q
q = series_sum(2)  # "1.25"
q
q = series_sum(3)  # "1.39"
q
q = series_sum(5)  # "1.57"
# => 1/1 + 1/4 + 1/7 + 1/10 + 1/13
q
