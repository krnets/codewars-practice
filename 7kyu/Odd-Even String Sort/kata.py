# from itertools import islice


# def sort_my_string(s):
#     even = "".join(islice(s, 0, len(s), 2))
#     odd  = "".join(islice(s, 1, len(s), 2))
#     return even + " " + odd


def sort_my_string(s):
    return s[::2] + " " + s[1::2]


# def sort_my_string(s):
#     return f'{s[::2]} {s[1::2]}'

q = sort_my_string("CodeWars")  # "CdWr oeas"
q
q = sort_my_string("YCOLUE'VREER")  # "YOU'RE CLEVER"
q
