import codewars_test as test
from kata import you_are_a_cube

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(you_are_a_cube(27),True)
        test.assert_equals(you_are_a_cube(1),True)
        test.assert_equals(you_are_a_cube(2),False)
        test.assert_equals(you_are_a_cube(99),False)
        test.assert_equals(you_are_a_cube(64),True)
