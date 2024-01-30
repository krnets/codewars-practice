import codewars_test as test
from kata import sort_array

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
        test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
        test.assert_equals(sort_array([]),[])
        test.assert_equals(sort_array([5, 3, 2, 8, 1, 4, 11]), [1, 3, 2, 8, 5, 4, 11])
        test.assert_equals(sort_array([2, 22, 37, 11, 4, 1, 5, 0]), [2, 22, 1, 5, 4, 11, 37, 0])
        test.assert_equals(sort_array([1, 111, 11, 11, 2, 1, 5, 0]),[1, 1, 5, 11, 2, 11, 111, 0])
        test.assert_equals(sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),[1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        test.assert_equals(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        test.assert_equals(sort_array([0, 1, 2, 3, 4, 9, 8, 7, 6, 5]),[0, 1, 2, 3, 4, 5, 8, 7, 6, 9])