import codewars_test as test
from kata import mobile_keyboard

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(mobile_keyboard(""), 0)
        test.assert_equals(mobile_keyboard("123"), 3)
        test.assert_equals(mobile_keyboard("codewars"), 26)
        test.assert_equals(mobile_keyboard("zruf"),16)
        test.assert_equals(mobile_keyboard("thisisasms"), 37)
        test.assert_equals(mobile_keyboard("longwordwhichdontreallymakessense"),107)