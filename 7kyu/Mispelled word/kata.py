from itertools import zip_longest


# def mispelled(word1, word2):
#     case_a = word1 in word2 and len(word1) == len(word2) - 1
#     case_b = word2 in word1 and len(word2) == len(word1) - 1
#     case_c = sum(x != y for x, y in zip_longest(word1, word2)) <= 1
#     return case_a or case_b or case_c


# def mispelled(word1, word2):
#     diff = len(word1) - len(word2)
#     if diff == 0:
#         return sum(x != y for x, y in zip(word1, word2)) <= 1
#     return word1 in word2 if diff == -1 else word2 in word1 if diff == 1 else False


def mispelled(word1, word2):
    match len(word1) - len(word2):
        case -1: return word1 in word2
        case 0: return sum(x != y for x, y in zip(word1, word2)) <= 1
        case 1: return word2 in word1
        case _: return False
