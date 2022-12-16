# def fold_to(distance):
#     if distance < 0:
#         return None

#     paper_thickness = 0.0001
#     folds = 0

#     while paper_thickness < distance:
#         paper_thickness *= 2
#         folds += 1

#     return folds


from math import ceil, log2


def fold_to(distance):
    if distance < 0:
        return None

    paper_thickness = 0.0001

    return ceil(log2(distance / paper_thickness)) if distance > paper_thickness else 0


q = fold_to(384000000)  # 42
q
q = fold_to(0.00005)  # 0
q
q = fold_to(0.0000001)  # 0
q
q = fold_to(0)  # 0
q
q = fold_to(-1)  # None
q
