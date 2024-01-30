import codewars_test as test
from kata import convert_bits


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(convert_bits(31, 14), 2)
        test.assert_equals(convert_bits(7, 17), 3)
        test.assert_equals(convert_bits(31, 0), 5)
        test.assert_equals(convert_bits(0, 0), 0)
        test.assert_equals(convert_bits(4222, 36363), 10)
        test.assert_equals(convert_bits(63283, 23258), 10)
        test.assert_equals(convert_bits(65206, 16183), 5)
