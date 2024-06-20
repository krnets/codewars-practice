# def what_list_am_i_on(actions):
#     count_naughty, count_nice = 0, 0

#     for s in actions:
#         for c in "bfk":
#             if s.startswith(c): count_naughty += 1
#         for c in "gsn":
#             if s.startswith(c): count_nice += 1
#     return ("nice", "naughty")[count_naughty >= count_nice]


def what_list_am_i_on(actions):
    count_naughty, count_nice = 0, 0

    for s in actions:
        if s.startswith(tuple("bfk")): count_naughty += 1
        elif s.startswith(tuple("gsn")): count_nice += 1
    return ("nice", "naughty")[count_naughty >= count_nice]
