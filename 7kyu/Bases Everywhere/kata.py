# def base_finder(seq):
#     return 1 + max(int(c) for c in "".join(seq))


# def base_finder(seq):
#     return 1 + max(map(int, "".join(seq)))


# def base_finder(seq):
#     return len(set("".join(seq)))


def base_finder(seq):
    return 1 + int(max("".join(seq)))
