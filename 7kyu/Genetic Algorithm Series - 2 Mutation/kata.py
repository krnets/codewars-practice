from random import random as rand
import re


# def mutate(chromosome, p):
#     res = ""

#     for c in chromosome:
#         if random.random() < p:
#             res += ("0", "1")[c == "0"]
#         else:
#             res += c

#     return res


# def mutate(chromosome, p):
#     return "".join(("0", "1")[c == "0"] if rand() < p else c for c in chromosome)


# def mutate(chromosome, p):
#     return re.sub(".", lambda m: ("0", "1")[m.group() == "0"] if rand() < p else m.group(), chromosome)


def mutate(chromosome, p):
    return re.sub(".", lambda m: "01"[m.group() == "0"] if rand() < p else m.group(), chromosome)
