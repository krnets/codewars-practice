import codewars_test as test
from solution import is_valid_HK_phone_number, has_valid_HK_phone_number


@test.describe("Basic tests")
def basic_tests():

    @test.it("is_valid_HK_phone_number")
    def is_valid_hk_phone_number():
        test.assert_equals(is_valid_HK_phone_number("1234 5678"), True)
        test.assert_equals(is_valid_HK_phone_number("2359 1478"), True)
        test.assert_equals(is_valid_HK_phone_number("85748475"), False)
        test.assert_equals(is_valid_HK_phone_number("3857  4756"), False)
        test.assert_equals(is_valid_HK_phone_number("sklfjsdklfjsf"), False)
        test.assert_equals(is_valid_HK_phone_number(
            "     1234 5678   "), False)
        test.assert_equals(is_valid_HK_phone_number("abcd efgh"), False)
        test.assert_equals(is_valid_HK_phone_number("9684 2396"), True)
        test.assert_equals(is_valid_HK_phone_number("836g 2986"), False)
        test.assert_equals(is_valid_HK_phone_number("0000 0000"), True)
        test.assert_equals(is_valid_HK_phone_number("123456789"), False)
        test.assert_equals(is_valid_HK_phone_number(" 987 634 "), False)
        test.assert_equals(is_valid_HK_phone_number("    6    "), False)
        test.assert_equals(is_valid_HK_phone_number("8A65 2986"), False)
        test.assert_equals(is_valid_HK_phone_number("8368 2aE6"), False)
        test.assert_equals(is_valid_HK_phone_number("8c65 2i86"), False)

    @test.it("has_valid_HK_phone_number")
    def has_valid_hk_phone_number():
        test.assert_equals(has_valid_HK_phone_number(
            "Hello, my phone number is 1234 5678"), True)
        test.assert_equals(has_valid_HK_phone_number(
            "I wonder if 2359 1478 is a valid phone number?"), True)
        test.assert_equals(has_valid_HK_phone_number(
            "85748475 is definitely invalid"), False)
        test.assert_equals(has_valid_HK_phone_number(
            "'3857  4756' is so close to a valid phone number!"), False)
        test.assert_equals(has_valid_HK_phone_number("sklfjsdklfjsf"), False)
        test.assert_equals(has_valid_HK_phone_number(
            "     1234 5678   "), True)
        test.assert_equals(has_valid_HK_phone_number(
            "What about abcd efgh?"), False)
        test.assert_equals(has_valid_HK_phone_number(
            "What about 9684 2396?"), True)
        test.assert_equals(has_valid_HK_phone_number("And 836g 2986?"), False)
        test.assert_equals(has_valid_HK_phone_number(
            "skldfjsdklfjs0000 0000skldfjslkdfjs"), True)
        test.assert_equals(has_valid_HK_phone_number(
            "123456789 is invalid"), False)
        test.assert_equals(has_valid_HK_phone_number(
            "sdfssdfsdfdf 987 634 sdfsddsds"), False)
        test.assert_equals(has_valid_HK_phone_number(
            "\n\n    6    \n\n"), False)
        test.assert_equals(has_valid_HK_phone_number(
            "sdfsdsdfdf8A65 2986sdfsddfs"), False)
        test.assert_equals(has_valid_HK_phone_number(
            "iwoeurwoeuwo8368 2aE6"), False)
        test.assert_equals(has_valid_HK_phone_number(
            "8c65 2i86wioeruwioeruweoi"), False)
