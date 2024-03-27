# def counting_valleys(s):
#     level = 0
#     exit_counter = 0
#     in_the_valley = False

#     for c in s:
#         if c == "U":
#             level += 1
#             if level == 0 and in_the_valley:
#                 exit_counter += 1
#                 in_the_valley = False
#         elif c == "D":
#             level -= 1
#             if level == -1:
#                 in_the_valley = True

#     return exit_counter


def counting_valleys(s):
    level, exit_counter = 0, 0

    for c in s:
        if c == "U":
            level += 1
            if level == 0:
                exit_counter += 1
        elif c == "D":
            level -= 1

    return exit_counter
