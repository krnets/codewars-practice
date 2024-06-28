from collections import Counter
import codewars_test as test


# def scramble(s1, s2):
#     freq = Counter(s1)

#     for c in s2:
#         if c in freq:
#             freq[c] -= 1
#             if freq[c] < 0:
#                 return False
#         else:
#             return False
#     return True


# def scramble(s1, s2):
#     return not len(Counter(s2) - Counter(s1))


def scramble(s1, s2):
    return Counter(s2) <= Counter(s1)


def dotest(s1, s2, expected):
    actual = scramble(s1, s2)
    test.assert_equals(actual, expected, f'With\ns1 = "{s1}"\ns2 = "{s2}"')


@test.describe("Tests")
def test_group():

    @test.it("Sample tests")
    def test_case():
        for s1, s2, expected in [
            ("rkqodlw", "world", True),
            ("cedewaraaossoqqyt", "codewars", True),
            ("katas", "steak", False),
            ("scriptjava", "javascript", True),
            ("scriptingjava", "javascript", True),
        ]:
            dotest(s1, s2, expected)

    @test.it("Example large test")
    def large_test():
        s1 = "abcdefghijklmnopqrstuvwxyz" * 10_000
        s2 = "zyxcba" * 9_000
        dotest(s1, s2, True)
