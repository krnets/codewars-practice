# def is_age_diverse(lst):
#     is_teen = lambda x: 11 <= x <= 19
#     is_twenties = lambda x: 20 <= x <= 29
#     is_thirties = lambda x: 30 <= x <= 39
#     is_forties = lambda x: 40 <= x <= 49
#     is_fifties = lambda x: 50 <= x <= 59
#     is_sixties = lambda x: 60 <= x <= 69
#     is_seventies = lambda x: 70 <= x <= 79
#     is_eighties = lambda x: 80 <= x <= 89
#     is_nineties = lambda x: 90 <= x <= 99
#     is_centenarian = lambda x: 100 <= x <= 199

#     fns = [is_teen, is_twenties, is_thirties, is_forties, is_fifties,
#            is_sixties, is_seventies, is_eighties, is_nineties, is_centenarian ]

#     for fn in fns:
#         if not any(fn(dev["age"]) for dev in lst):
#             return False

#     return True


# def is_age_diverse(lst):
#     return len(set(min(dev["age"] // 10, 10) for dev in lst) - {0}) == 10


# def is_age_diverse(lst):
#     return sum(set(min(dev["age"] // 10, 10) for dev in lst)) == sum(range(11))


# def is_age_diverse(lst):
#     age_ranges = [False] * 10
#     for dev in lst:
#         age_ranges[(9, dev["age"] // 10 - 1)[dev["age"] < 100]] = True
#     return all(age_ranges)


def is_age_diverse(lst):
    return set(range(1, 10)).issubset(dev["age"] // 10 for dev in lst)
