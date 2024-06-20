import codewars_test as test
from kata import print_nums


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(print_nums(), "")
        test.assert_equals(print_nums(2), "2")
        test.assert_equals(print_nums(1, 12, 34), "01\n12\n34")
        test.assert_equals(print_nums(1009, 2), "1009\n0002")
        test.assert_equals(print_nums(1, 1, 13), "01\n01\n13")
        test.assert_equals(print_nums(*range(2, 10, 3)), "2\n5\n8")
        test.assert_equals(print_nums(*(i**3 for i in range(1, 4))), "01\n08\n27")
