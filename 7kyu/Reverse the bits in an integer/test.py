import codewars_test as test
from kata import reverse_bits


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(reverse_bits(417), 267)
        test.assert_equals(reverse_bits(267), 417)
        test.assert_equals(reverse_bits(0), 0)
        test.assert_equals(reverse_bits(2017), 1087)
        test.assert_equals(reverse_bits(1023), 1023)
        test.assert_equals(reverse_bits(1024), 1)
