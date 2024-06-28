import codewars_test as test


# def expanded_form(num):
#     decimal, fraction = str(num).split(".")
#     ans, left, right = "", [], []

#     for i, c in enumerate(decimal):
#         if c != "0":
#             left.append(c.ljust(len(decimal) - i, "0"))

#     if len(left) > 0:
#         ans += " + ".join(left)

#     for i, c in enumerate(fraction, 2):
#         if c != "0":
#             right.append(c + "/" + "1".ljust(i, "0"))

#     if len(right) > 0:
#         if len(ans) > 0:
#             ans += " + "
#         ans += " + ".join(right)
#     return ans


def expanded_form(num):
    decimal, fraction = str(num).split(".")
    res = []

    for i, c in enumerate(decimal):
        if c != "0":
            res.append(c.ljust(len(decimal) - i, "0"))

    for i, c in enumerate(fraction, 2):
        if c != "0":
            res.append(c + "/" + "1".ljust(i, "0"))

    return " + ".join(res)


@test.describe("Example tests")
def example_tests():

    @test.it("Examples")
    def examples():
        test.assert_equals(expanded_form(1.24), "1 + 2/10 + 4/100")
        test.assert_equals(expanded_form(7.304), "7 + 3/10 + 4/1000")
        test.assert_equals(expanded_form(0.04), "4/100")
        test.assert_equals(expanded_form(807.304), "800 + 7 + 3/10 + 4/1000")
