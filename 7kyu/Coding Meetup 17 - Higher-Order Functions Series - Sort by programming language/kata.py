# def sort_by_language(arr):
#     return sorted(arr, key=lambda d: (d["language"], d["first_name"]))


from operator import itemgetter


def sort_by_language(arr):
    return sorted(arr, key=itemgetter("language", "first_name"))
