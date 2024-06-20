# def t_area(t_str):
#     n = len(t_str.split("\n")) - 3
#     return n**2 / 2


def t_area(t_str):
    n = t_str.count("\n") - 2
    return n**2 / 2
