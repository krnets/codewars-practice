# 7kyu - Sum of all the multiples of 3 or 5

"""   Write function find

Upto and including n, this function will return the sum of all multiples of 3 and 5.

find(5) should return 8 (3 + 5)
find(10) should return 33 (3 + 5 + 6 + 9 + 10) """


def find(n):
    return sum(x for x in range(1, n+1) if x % 3 == 0 or x % 5 == 0)


q = find(5)  # 8
q
q = find(10)  # 33
q
