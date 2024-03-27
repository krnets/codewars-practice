import codewars_test as test
from kata import shuffled_array

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(shuffled_array([1, 12, 3, 6, 2]),[1, 2, 3, 6])
        test.assert_equals(shuffled_array([1, -3, -5, 7, 2]),[-5, -3, 2, 7])
        test.assert_equals(shuffled_array([2, -1, 2, 2, -1]),[-1, -1, 2, 2])
        test.assert_equals(shuffled_array([-3, -3]),[-3])