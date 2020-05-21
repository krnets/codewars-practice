# 6kyu - Build Tower Advanced

""" Build Tower by the following given arguments:
number of floors (integer and always greater than 0)
block size (width, height) (integer pair and always greater than (0, 0))

Tower block unit is represented as *

for example, a tower of 3 floors with block size = (2, 3) looks like below
[
  '    **    ',
  '    **    ',
  '    **    ',
  '  ******  ',
  '  ******  ',
  '  ******  ',
  '**********',
  '**********',
  '**********'
]
and a tower of 6 floors with block size = (2, 1) looks like below
[
  '          **          ', 
  '        ******        ', 
  '      **********      ', 
  '    **************    ', 
  '  ******************  ', 
  '**********************'
] """

# def tower_builder(n_floors, block_size):
#     w, h = block_size
#     tower = []
#     for i in range(n_floors):
#         for _ in range(h):
#             row = '*' * (w + i * (w * 2))
#             pad = ' ' * ((n_floors - i) * w - w)
#             tower.append(pad + row + pad)
#     return tower


# def tower_builder(n_floors, block_size):
#     w, h = block_size
#     return [("*" * (i*2-1)*w).center((n_floors*2-1)*w) for i in range(1, n_floors+1) for _ in range(h)]

# def tower_builder(n_floors, block_size):
#     w, h = block_size
#     return [f"{'*' * w * (2*i + 1):^{(n_floors*2 - 1) * w}}" for i in range(n_floors) for _ in range(h)]

def tower_builder(n_floors, block_size):
    w, h = block_size
    row_len = w * (2 * n_floors - 1)
    return [("*" * i).center(row_len) for i in range(w, row_len+1, 2 * w) for _ in range(h)]


q = tower_builder(1, (1, 1))  # ['*', ]
q
q = tower_builder(3, (4, 2))
# ['        ****        ', '        ****        ', '    ************    ', '    ************    ', '********************', '********************'])
q
q = tower_builder(3, (2, 3))
q
