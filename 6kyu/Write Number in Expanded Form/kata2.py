from math import log10
import codewars_test as test


# def expanded_form(num):
#     expanded = []
#     m = 1

#     while num:
#         expanded.append(num % 10 * m)
#         num //= 10
#         m *= 10

#     return " + ".join(str(x) for x in reversed(expanded) if x)


def expanded_form(num):
    expanded = []

    for i in range(int(log10(num)), -1, -1):
        exp = 10**i
        quotient, num = divmod(num, exp)
        if quotient:
            expanded.append(quotient * exp)

    return " + ".join(map(str, expanded))


@test.describe("Sample tests")
def sample_tests():

    @test.it("Should pass sample tests")
    def should_pass_sample_tests():
        test.assert_equals(expanded_form(12), "10 + 2")
        test.assert_equals(expanded_form(42), "40 + 2")
        test.assert_equals(expanded_form(70304), "70000 + 300 + 4")
