from itertools import chain
from random import randrange, sample


# def get_bingo_card():
#     b_col, i_col, n_col, g_col, o_col = (set() for _ in range(5))

#     while len(b_col) < 5: b_col.add("B" + str(randrange(1, 16)))
#     while len(i_col) < 5: i_col.add("I" + str(randrange(16, 31)))
#     while len(n_col) < 4: n_col.add("N" + str(randrange(31, 46)))
#     while len(g_col) < 5: g_col.add("G" + str(randrange(46, 61)))
#     while len(o_col) < 5: o_col.add("O" + str(randrange(61, 76)))

#     return [*chain.from_iterable([b_col, i_col, n_col, g_col, o_col])]


# def get_bingo_card():
#     b = ["B%s" % x for x in sample(range(1, 16), 5)]
#     i = ["I%s" % x for x in sample(range(16, 31), 5)]
#     n = ["N%s" % x for x in sample(range(31, 46), 4)]
#     g = ["G%s" % x for x in sample(range(46, 61), 5)]
#     o = ["O%s" % x for x in sample(range(61, 76), 5)]
#     return b + i + n + g + o


def get_bingo_card():
    return [
        c + str(x + 1)
        for i, c in enumerate("BINGO")
        for x in sample(range(i * 15, (i + 1) * 15), 5 - (i == 2))
    ]
