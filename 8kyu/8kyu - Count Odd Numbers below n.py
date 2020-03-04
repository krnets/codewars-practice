# 8kyu - Count Odd Numbers below n

""" Given a number n, return the number of positive odd numbers below n, EASY!

oddCount(7) //=> 3, i.e [1, 3, 5]
oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]

Expect large Inputs! """


# def odd_count(n):
#     return n // 2

def odd_count(n):
    return len(range(1, n, 2))

# def odd_count(n):
#     return n >> 1

q = odd_count(15)  # 7
q
q = odd_count(15023)  # 7511
q
