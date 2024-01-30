from operator import itemgetter


# def scramble(strng, array):
#     return "".join(map(itemgetter(0), sorted(zip(strng, array), key=itemgetter(1))))


def scramble(strng, array):
    return "".join(c for _, c in sorted(zip(array, strng)))
