# Beta - last digits of a number

""" Your job is to write function last_digits(n,d) which return the last d digits of an integer n as a list. 
n will be from 0 to 10^10

last_digits(1,1) --> [1]
last_digits(1234,2) --> [3,4]
last_digits(637547,6) --> [6,3,7,5,4,7]

Special cases:

If d > the number of digits, just return the number's digits as a list.
If d <= 0, then return an empty list. """


def solution(n, d):
    return [int(x) for x in list(str(n))[-d:]] if d > 0 else list()


# 'Example tests'
q = solution(1, 1)  # [1]
q
q = solution(123767, 4)  # [3,7,6,7]
q
q = solution(0, 1)  # [0]
q
q = solution(34625647867585, 10)  # [5,6,4,7,8,6,7,5,8,5]
q

# 'd <= 0'
q = solution(1234, 0)  # []
q
q = solution(24134, -4)  # []
q

# 'd > number of digits in n'
q = solution(1343, 5)  # [1,3,4,3]
q
