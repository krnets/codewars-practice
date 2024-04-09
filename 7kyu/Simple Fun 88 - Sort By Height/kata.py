def sort_by_height(a):
    sorted_a = filter(lambda x: x > 0, sorted(a))
    return [x if x < 0 else next(sorted_a) for x in a]
