import codewars_test as test
from kata import solution


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(solution("helloWorld"), "hello World")
        test.assert_equals(solution("identifier"), "identifier")
        test.assert_equals(solution("camelCase"), "camel Case")
        test.assert_equals(solution("breakCamelCase"), "break Camel Case")
        test.assert_equals(solution("consecutiveCApitals"), "consecutive C Apitals")
