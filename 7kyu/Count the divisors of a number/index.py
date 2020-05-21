# 7kyu - Count the divisors of a number

""" Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

divisors(4)  == 3  # 1, 2, 4
divisors(5)  == 2  # 1, 5
divisors(12) == 6  # 1, 2, 3, 4, 6, 12
divisors(30) == 8  # 1, 2, 3, 5, 6, 10, 15, 30 """

# def divisors(n):
#     divs = []
#     for x in range(1, n+1):
#         if n % x == 0:
#             divs.append(x)
#     return len(divs)

# def divisors(n):
#     count = 0
#     for x in range(1, n+1):
#         if n % x == 0:
#             count += 1
#     return count


# def divisors(n):
#     count = 1
#     for x in range(1, n//2+1):
#         if n % x == 0:
#             count += 1
#     return count

def divisors(n):
    return sum(1 for x in range(1, n // 2 + 1) if n % x == 0) + 1


q = divisors(4)  # 3
q
q = divisors(5)  # 2
q
q = divisors(12)  # 6
q
q = divisors(30)  # 8
q
q = divisors(4096)  # 13
q
