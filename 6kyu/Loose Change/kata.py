# from operator import itemgetter

# denominations = {"Pennies": 1, "Nickels": 5, "Dimes": 10, "Quarters": 25}


# def loose_change(cents):
#     ret_change = {k: 0 for k in denominations.keys()}

#     if cents < 0:
#         return ret_change

#     for k, v in sorted(denominations.items(), key=itemgetter(1), reverse=True):
#         n_coins = cents // v
#         cents -= n_coins * v
#         ret_change[k] = n_coins

#     return ret_change

from collections import OrderedDict

denominations = OrderedDict(Quarters=25, Dimes=10, Nickels=5, Pennies=1)


def loose_change(cents) -> dict:
    ret_change = {k: 0 for k in denominations.keys()}

    if cents <= 0:
        return ret_change

    for k, v in denominations.items():
        n_coins = cents // v
        cents -= n_coins * v
        ret_change[k] = n_coins

    return ret_change
