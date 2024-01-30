from itertools import groupby
import re


# def solution(stones):
#     return sum(len(list(v)) - 1 for _, v in groupby(stones))


# def solution(stones):
#     return len(stones) - len(re.sub(r"([RGB])(\1+)", r"\1", stones))


def solution(stones):
    return len(re.findall(r"(?=(RR|GG|BB))", stones))
