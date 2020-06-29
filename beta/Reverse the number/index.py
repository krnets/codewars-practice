""" Beta - Reverse the number

Reverse the integer without using strings or lists

reverse(123456) -> 654321 """


def reverse(n):
    rev = 0
    while n:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev


q = reverse(123456), 654321
q
q = reverse(0), 0
q
q = reverse(100), 1
q
q = reverse(1234567891011), 1101987654321
q
