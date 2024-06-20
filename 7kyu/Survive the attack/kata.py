from itertools import zip_longest

def is_defended(attackers, defenders):
    a_survivors, d_survivors = 0, 0

    for a, d in zip_longest(attackers, defenders, fillvalue=0):
        if a > d: a_survivors += 1
        elif d > a: d_survivors += 1

    if a_survivors > d_survivors: return False
    if d_survivors > a_survivors: return True
    return sum(defenders) >= sum(attackers)
