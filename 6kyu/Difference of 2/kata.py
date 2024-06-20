# def twos_difference(lst):
#     return sorted((x, x + 2) for x in lst if x + 2 in lst)


def twos_difference(lst):
    uniq_vals = set(lst)
    return sorted((x, x + 2) for x in lst if x + 2 in uniq_vals)
