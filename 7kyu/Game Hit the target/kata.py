# def solution(mtrx):
#     for row in mtrx:
#         if ">" in row and "x" in row:
#             return row.index(">") < row.index("x")
#     return False


def solution(mtrx):
    return next((row.index(">") < row.index("x") for row in mtrx if ">" in row and "x" in row), False)
