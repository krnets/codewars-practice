from operator import itemgetter


# def sort_reindeer(reindeer_names):
#     splits = [name.split() for name in reindeer_names]
#     # return [" ".join(name) for name in sorted(splits, key=lambda x: x[1])]
#     return [" ".join(name) for name in sorted(splits, key=itemgetter(1))]


def sort_reindeer(reindeer_names):
    return sorted(reindeer_names, key=lambda s: s.split()[1])
