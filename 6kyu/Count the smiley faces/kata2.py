import re
import codewars_test as test


# def count_smileys(arr):
#     ans = 0
#     for x in arr:
#         if x[0] in (":", ";") and x[-1] in (")", "D"):
#             if len(x) == 2:
#                 ans += 1
#             elif len(x) == 3 and x[1] in ("-", "~"):
#                 ans += 1
#     return ans


# def count_smileys(arr):
#     return len(re.findall(r"[:;][-~]?[)D]", " ".join(arr)))


def count_smileys(arr):
    return sum(bool(re.fullmatch(r"[:;][-~]?[)D]", x)) for x in arr)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(count_smileys([]), 0)
        test.assert_equals(count_smileys([":D", ":~)", ";~D", ":)"]), 4)
        test.assert_equals(count_smileys([":)", ":(", ":D", ":O", ":;"]), 2)
        test.assert_equals(count_smileys([";]", ":[", ";*", ":$", ";-D"]), 1)
