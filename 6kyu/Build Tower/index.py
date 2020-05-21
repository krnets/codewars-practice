# 6kyu - Build Tower

""" Build Tower by the following given argument: number of floors (integer and always greater than 0).
Tower block is represented as *
for example, a tower of 3 floors looks like below
[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below
[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
] """


# def tower_builder(n_floors):
#     res = []
#     for i in range(1, n_floors+1):
#         row = '*' * (i * 2 - 1)
#         pad = ' ' * (n_floors - i)
#         res.append(pad + row + pad)
#     return res

# def tower_builder(n_floors):
#     return [("*" * (i*2-1)).center(n_floors*2-1) for i in range(1, n_floors+1)]

def tower_builder(n_floors):
    width = n_floors*2-1
    return [("*" * (i*2-1)).center(width) for i in range(1, n_floors+1)]


q = tower_builder(1)  # ['*', ]
q
q = tower_builder(2)  # [' * ', '***']
q
q = tower_builder(3)  # ['  *  ', ' *** ', '*****']
q
