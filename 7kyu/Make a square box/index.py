# 7kyu - Make a square box!

""" Given a number as a parameter, return an array containing strings which form a box.
Like this:

n = 5

[
  '-----',
  '-   -',
  '-   -',
  '-   -',
  '-----'
]

n = 3

[
  '---',
  '- -',
  '---'
] """


# def box(n):
#     res = []
#     res.append('-' * n)
#     if n > 2:
#         for i in range(n-2):
#             res.append('-' + ' ' * (n-2) + '-')
#     res.append('-' * n)
#     return res

def box(n):
    outter = '-' * n
    inner = '-' + ' ' * (n-2) + '-'
    return [outter] + [inner] * (n-2) + [outter]


q = box(5)
q
# ['-----', '-   -', '-   -', '-   -', '-----']
