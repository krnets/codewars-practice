# 7kyu - 8 towers

""" Marcus was spending his last summer day playing chess with his friend Rose.

Surprisingly, they had a lot of pieces (we suspect Marcus is a part-time thief, 
but we will leave that aside), and Marcus wondered in how many different positions 
could 8 towers (rooks) be in the board, without threatening themselves.

Rose (who was smarter) was wondering if there was any relation between the 
size of the board, and the number of positions.

So, you should help!

Write a function that, given N (positive-only integer) the size of the board, 
returns the number of different combinations in which these towers can be.

Example:

towerCombination(2) returns 2, because only the following possibilities can be achieved.

| x 0 |
| 0 x |

| 0 x |
| x 0 |

towerCombination(3) returns 6, because only the following possibilities can be achieved.

| x 0 0 |
| 0 x 0 |
| 0 0 x |

| x 0 0 |
| 0 0 x |
| 0 x 0 |

| 0 x 0 |
| x 0 0 |
| 0 0 x |

| 0 x 0 |
| 0 0 x |
| x 0 0 |

| 0 0 x |
| x 0 0 |
| 0 x 0 |

| 0 0 x |
| 0 x 0 |
| x 0 0 | """

# def tower_combination(n):
#     if n == 1:
#         return 1
#     return n * tower_combination(n-1)

# def tower_combination(n):
#     return 1 if n == 1 else n * tower_combination(n-1)

# from math import factorial

# def tower_combination(n):
#     return factorial(n)

from math import factorial as tower_combination

q = tower_combination(2),  2
q
q = tower_combination(3),  6
q
