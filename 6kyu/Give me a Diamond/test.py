import codewars_test as test
from kata import diamond


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        expected = " *\n"
        expected += "***\n"
        expected += " *\n"
        test.assert_equals(diamond(1), "*\n")
        test.assert_equals(diamond(2), None)
        test.assert_equals(diamond(3), expected)
        test.assert_equals(diamond(5), "  *\n ***\n*****\n ***\n  *\n")
        test.assert_equals(diamond(0), None)
        test.assert_equals(diamond(-3), None)
