import codewars_test as test
from kata import single_digit


@test.describe("sample tests")
def fixed_tests():
    @test.it("should return a single digit integer")
    def basic_test_cases():
        test.assert_equals(single_digit(5665), 5)
        test.assert_equals(single_digit(123456789), 1)
