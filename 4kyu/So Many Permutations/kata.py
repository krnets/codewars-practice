import codewars_test as test
from itertools import permutations as helper


# def permutations(s):
#     return list(set(map("".join, permute(s))))


# def permutations(s):
#     return list(map("".join, set(permute(s))))


# def permutations(s):
#     return helper(s)


# def helper(st, p=[]):
#     if not st:
#         yield "".join(p)
#     else:
#         seen = set()
#         for i, c in enumerate(st):
#             if c not in seen:
#                 p.append(c)
#                 seen.add(c)
#                 yield from helper(st[:i] + st[i + 1 :], p)
#                 p.pop()


def permutations(st, p=[]):
    if not st:
        yield "".join(p)
    else:
        seen = set()
        for i, c in enumerate(st):
            if c not in seen:
                p.append(c)
                seen.add(c)
                yield from permutations(st[:i] + st[i + 1 :], p)
                p.pop()


@test.describe("Basic Tests")
def basic_tests():

    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(sorted(permutations("a")), ["a"])
        test.assert_equals(sorted(permutations("ab")), ["ab", "ba"])
        test.assert_equals(
            sorted(permutations("aabb")),
            ["aabb", "abab", "abba", "baab", "baba", "bbaa"],
        )
