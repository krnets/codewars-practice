# def solution(n, d):
#     return [*map(int, str(n))][-d:] if d > 0 else []


def solution(n, d):
    return [*map(int, str(n)[-d:])] if d > 0 else []
