from itertools import groupby, pairwise
import re

# def count_adjacent_pairs(st):
#     ans, last_pair = 0, None

#     for fst, snd in pairwise(st.lower().split()):
#         if fst == snd:
#             if (fst, snd) != last_pair:
#                 ans += 1
#             last_pair = fst, snd
#     return ans


# def count_adjacent_pairs(st):
#     return sum(1 for _, g in groupby(st.lower().split()) if len(list(g)) > 1)


def count_adjacent_pairs(st):
    return len(re.findall(r"(\b\w+)(\s\1)+", st, re.I))
