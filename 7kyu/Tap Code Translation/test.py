import codewars_test as test
from kata import tap_code_translation

@test.describe("Example Tests")
def example_tests():
    test.assert_equals(tap_code_translation("breaks"), ". .. .... .. . ..... . . . ... .... ...")
    test.assert_equals(tap_code_translation("taps"), ".... .... . . ... ..... .... ...")
    test.assert_equals(tap_code_translation("knocks"), ". ... ... ... ... .... . ... . ... .... ...")