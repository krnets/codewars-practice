def get_missing_element(seq):
    n = len(seq)
    return n * (n + 1) // 2 - sum(seq)


q = get_missing_element([0, 5, 1, 3, 2, 9, 7, 6, 4])  # 8
q
q = get_missing_element([9, 2, 4, 5, 7, 0, 8, 6, 1])  # 3
q
