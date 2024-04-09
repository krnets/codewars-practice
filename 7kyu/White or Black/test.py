import codewars_test as test
from kata import square_color

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(square_color("a", 8), "white")
        test.assert_equals(square_color("b", 2), "black")
        test.assert_equals(square_color("f", 5), "white")