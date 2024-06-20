from itertools import zip_longest, chain
import codewars_test as test


# def interweave(s1, s2):
#     ans = ""
#     for a, b in zip_longest(s1, s2, fillvalue=" "):
#         if not a.isdigit(): ans += a
#         if not b.isdigit(): ans += b
#     return ans.strip()


def interweave(s1, s2):
    return "".join(
        c
        for c in chain.from_iterable(zip_longest(s1, s2, fillvalue=""))
        if not c.isdigit()
    )


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(interweave("", ""), "")
        test.assert_equals(interweave("hlo", "el"), "hello")
        test.assert_equals(interweave("h3lo", "el4"), "hello")
