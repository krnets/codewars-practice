def repeat_adjacent(st):
    chars = list(st)
    prev_char = ""
    curr_char_count = 1

    for i, c in enumerate(chars):
        if prev_char == c:
            curr_char_count += 1
        else:
            prev_char = c
            if curr_char_count == 1:
                chars[i - 1] = "_"
            curr_char_count = 1

    return len([x for x in filter(None, "".join(chars).split("_")) if len(set(x)) > 1])


# from itertools import groupby
# import re


# def repeat_adjacent(st):
#     g_lens = [len(list(g)) for _, g in groupby(st)]
#     return sum(k for k, v in groupby(g_lens, key=lambda x: x > 1) if len(list(v)) > 1)


# def repeat_adjacent(st):
#     pattern = r"((.)\2+(?!\2)){2,}"
#     return len(re.findall(pattern, st))
