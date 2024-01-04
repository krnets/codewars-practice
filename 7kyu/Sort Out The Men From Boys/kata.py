from itertools import filterfalse


# def men_from_boys(arr):
#     unique = set(arr)
#     men = [*sorted(filterfalse(is_odd, unique))]
#     boys = [*sorted(filter(is_odd, unique), reverse=True)]
#     return men + boys


def men_from_boys(arr):
    men = {*filterfalse(is_odd, arr)}
    boys = {*filter(is_odd, arr)}
    return [*sorted(men)] + [*sorted(boys, reverse=True)]


def is_odd(n):
    return n % 2 == 1
