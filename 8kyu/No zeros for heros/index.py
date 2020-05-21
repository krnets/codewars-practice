# 8kyu - No zeros for heros

""" Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105

Zero alone is fine, don't worry about it. Poor guy anyway """


# def no_boring_zeros(n):
#     res = []
#     arr = list(str(n))[::-1]
#     for i in range(0, len(arr)):
#         if arr[i] != '0':
#             return int(''.join(reversed(arr[i:])))
#     return 0

# def no_boring_zeros(n):
#     return int(str(n).rstrip('0')) if n else n

# def no_boring_zeros(n):
#     return int(str(n).rstrip('0') or '0')

def no_boring_zeros(n):
    while n and n % 10 == 0:
        n /= 10
    return n

q = no_boring_zeros(1450)  # 145
q
q = no_boring_zeros(960000)  # 96
q
q = no_boring_zeros(1050)  # 105
q
q = no_boring_zeros(-1050)  # -105
q
q = no_boring_zeros(0)  # 0
q
