# 7kyu - Share prices

""" You spent all your saved money to buy some shares.

You bought it for invested, and want to know how much it's worth, but all the info you can quickly get 
are just the change the shares price made in percentages.

Your task: Write the function sharePrice() that calculates, and returns the current price of your share, 
given the following two arguments:

    invested(number), the amount of money you initially invested in the given share
    changes(array of numbers), contains your shares daily movement percentages

The returned number, should be in string format, and it's precision should be fixed at 2 decimal numbers.
Try to write the function in a functional manner. """


# def share_price(invested, changed):
#     for x in changed:
#         invested *= 1 - abs(x * 0.01) if x < 0 else x * 0.01 + 1
#     return '{:.2f}'.format(invested)

# def share_price(invested, changed):
#     for percent in changed:
#         invested *= (100 + percent) / 100
#     return '{:.2f}'.format(invested)

# def share_price(invested, changed):
#     for percent in changed:
#         invested *= (100 + percent) / 100
#     return format(invested, '.2f')

from functools import reduce
from operator import mul

# def share_price(invested, changed):
#     return '{:.2f}'.format(reduce(lambda p, c: p * c, [x / 100 + 1 for x in changed], invested))

def share_price(invested, changed):
    return '{:.2f}'.format(reduce(lambda m, n: m * (1 + n/100), changed, invested))

# def share_price(invested, changed):
#     return '{:.2f}'.format(reduce(mul, [x/100 + 1 for x in changed], invested))


q = share_price(100, []), '100.00'
q
q = share_price(100, [-50, 50]), '75.00'
q
q = share_price(100, [-50, 100]), '100.00'
q
q = share_price(100, [-20, 30]), '104.00'
q
q = share_price(1000, [0, 2, 3, 6]), '1113.64'
q
