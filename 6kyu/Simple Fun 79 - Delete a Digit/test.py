import codewars_test as test
from kata import delete_digit


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(delete_digit(152), 52)
        test.assert_equals(delete_digit(1001), 101)
        test.assert_equals(delete_digit(10), 1)
