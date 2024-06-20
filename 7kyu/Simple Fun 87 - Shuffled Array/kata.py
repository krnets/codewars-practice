# def shuffled_array(s):
#     s.pop(s.index(sum(s) // 2))
#     return sorted(s)


def shuffled_array(s):
    s.sort()
    s.remove(sum(s) // 2)
    return s
