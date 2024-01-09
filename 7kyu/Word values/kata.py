# def name_value(my_list):
#     offset = ord("a") - 1
#     res = []

#     for index, word in enumerate(my_list, 1):
#         sum = 0
#         for c in word:
#             if c != " ":
#                 sum += ord(c) - offset
#         res.append(sum * index)

#     return res


# def name_value(my_list):
#     offset = ord("a") - 1

#     return [
#         i * sum(map(lambda c: ord(c) - offset, st.replace(" ", "")))
#         for i, st in enumerate(my_list, 1)
#     ]


def name_value(my_list):
    offset = ord("a") - 1

    return [
        i * sum(map(lambda c: ord(c) - offset if c != " " else 0, st))
        for i, st in enumerate(my_list, 1)
    ]
