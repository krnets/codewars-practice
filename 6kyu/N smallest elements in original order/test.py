import codewars_test as test
from kata import first_n_smallest

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(first_n_smallest([1,2,3,4,5],3), [1,2,3])
        test.assert_equals(first_n_smallest([5,4,3,2,1],3), [3,2,1])
        test.assert_equals(first_n_smallest([1,2,3,1,2],3), [1,2,1])
        test.assert_equals(first_n_smallest([1,2,3,-4,0],3), [1,-4,0])
        test.assert_equals(first_n_smallest([1,2,3,4,5],0), [])
        test.assert_equals(first_n_smallest([1,2,3,4,5],5), [1,2,3,4,5])
        test.assert_equals(first_n_smallest([1,2,3,4,2],4), [1,2,3,2])
        test.assert_equals(first_n_smallest([2,1,2,3,4,2],2), [2,1])
        test.assert_equals(first_n_smallest([2,1,2,3,4,2],3), [2,1,2])
        test.assert_equals(first_n_smallest([2,1,2,3,4,2],4), [2,1,2,2])
        test.assert_equals(first_n_smallest([4, -10, 10, 4, -7, 10, 5],3), [4, -10, -7])
        test.assert_equals(first_n_smallest([-3, -2, -8, -2, 4, 9, 8, -9, -4, 7, -4, 5], 6), [-3, -2, -8, -9, -4, -4])
        test.assert_equals(first_n_smallest([-10, 10, 2, -3, -9, -3, 7, 2, 3, -6, 9, 8, -8, 6, -5, -1, -3, -7, 0, -9, -5, -8, 0, 7, 5, -7, 4, 2, -6, 10, -5, 9, 2], 30), [-10, 2, -3, -9, -3, 7, 2, 3, -6, 9, 8, -8, 6, -5, -1, -3, -7, 0, -9, -5, -8, 0, 7, 5, -7, 4, 2, -6, -5, 2])