import codewars_test as test
import re


# def increment_string(strng):
#     if not strng or not strng[-1].isdigit():
#         return strng + "1"
#     digits = re.findall(r"\d+$", strng)[0]
#     n = len(digits)
#     return strng[:-n] + str(int(digits) + 1).zfill(n)


def increment_string(strng):
    digits = re.findall(r"\d+$", strng)
    if not digits:
        return strng + "1"
    n = len(digits[0])
    return f"{strng[:-n]}{int(digits[0]) + 1:0{n}}"


@test.describe("Basic Tests")
def basic_tests():

    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(increment_string("foo"), "foo1")
        test.assert_equals(increment_string("foobar001"), "foobar002")
        test.assert_equals(increment_string("foobar1"), "foobar2")
        test.assert_equals(increment_string("foobar00"), "foobar01")
        test.assert_equals(increment_string("foobar99"), "foobar100")
        test.assert_equals(increment_string("foobar099"), "foobar100")
        test.assert_equals(increment_string("fo99obar99"), "fo99obar100")
        test.assert_equals(increment_string(""), "1")
