from random import randint
import codewars_test as test
from kata import get_reversed_color


def build_not_hex_string():
    res = hex(randint(0, 16777215))[2:]
    l = len(res) / 2
    rand_char = chr(randint(103, 122))
    res = res[:l] + rand_char + res[l + 1 :]
    return res


def build_random_hex_string():
    return hex(randint(0, 16777215))[2:]


def build_too_large_string():
    return hex(randint(16777216, 2**60 - 1))[2:]


test.it("tests for getting the complementary color to the entered one")
test.assert_equals(
    get_reversed_color(""), "#FFFFFF", "Result should begins with hash-char - #"
)
test.assert_equals(
    get_reversed_color("0"), "#FFFFFF", "Result should begins with hash-char - #"
)
test.expect_error(
    "Invalid length value should throw error.", lambda: get_reversed_color("1234567")
)
test.expect_error(
    "Invalid character in hex_color should throw error.",
    lambda: get_reversed_color("AA00ZZ"),
)
test.expect_error(
    "Invalid type value should throw error.", lambda: get_reversed_color(0)
)
test.assert_equals(
    get_reversed_color("a124fb"),
    "#5EDB04",
)
