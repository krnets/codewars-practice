# def sentence(lst):
#     pairs = []

#     for d in lst:
#         idx, item = d.popitem()
#         pairs.append((int(idx), item))

#     pairs.sort(key=lambda x: x[0])

#     return " ".join(pair[1] for pair in pairs)


def sentence(lst):
    return " ".join(
        next(iter(d.values()))
        for d in sorted(lst, key=lambda d: int(next(iter(d.keys()))))
    )
