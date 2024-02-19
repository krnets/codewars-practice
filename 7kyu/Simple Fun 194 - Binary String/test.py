import codewars_test as test
from kata import bin_str


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(bin_str("0101"), 3)
        test.assert_equals(bin_str("10000"), 2)
        test.assert_equals(bin_str("0000000000"), 0)
        test.assert_equals(bin_str("1111111111"), 1)
        test.assert_equals(bin_str("10101010101010"), 14)
        test.assert_equals(bin_str("11111000011111"), 3)
        test.assert_equals(bin_str("000001111100000"), 2)
        test.assert_equals(bin_str("111000000000"), 2)
        test.assert_equals(bin_str("00000000111111111"), 1)
        test.assert_equals(bin_str("1010101011111111111111000000000"), 10)
