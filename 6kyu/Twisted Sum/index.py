# 6kyu - Twisted Sum

""" Find the sum of the digits of all the numbers from 1 to N (both ends included).

# N = 4
1 + 2 + 3 + 4 = 10

# N = 10
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46

# N = 12
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51 """

# def compute_sum(n):
#     return sum(int(x) for x in list(''.join(str(x) for x in list(range(n + 1)))))

# def compute_sum(n):
#     return sum(int(x) for x in ''.join(str(x) for x in range(n + 1)))

# def compute_sum(n):
#     return sum(int(c) for i in range(n+1) for c in str(i))

def compute_sum(n):
    return sum(map(int, ''.join(str(n) for n in range(n+1))))


q = compute_sum(1)  # 1
q
q = compute_sum(2)  # 3
q
q = compute_sum(3)  # 6
q
q = compute_sum(4)  # 10
q
q = compute_sum(10)  # 46
q
q = compute_sum(12)  # 51
q