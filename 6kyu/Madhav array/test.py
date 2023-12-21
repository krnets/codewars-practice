import codewars_test as test
from kata import is_madhav_array

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(is_madhav_array([2, 1, 1]), True)
        test.assert_equals(is_madhav_array([2, 1, 1, 4, -1, -1]), True)
        
    @test.it('Edge Cases')
    def basic_test_cases():
        test.assert_equals(is_madhav_array([6,2,4,2,2,2,1,5,0,0]),True)
        test.assert_equals(is_madhav_array([6,2,4,2,2,2,1,5,0,-100]),False)
        test.assert_equals(is_madhav_array([0,0,0,0,0,0,0,0,0,0,1,1,1,-2,-1]),True)
        test.assert_equals(is_madhav_array([-6,-3,-3,8,-5,-4]),False)
        test.assert_equals(is_madhav_array([-6,-3,-3,8,-10,-4]),True)
        test.assert_equals(is_madhav_array([3,1,2,3,0]),False)
        test.assert_equals(is_madhav_array([3,3]),False)
        test.assert_equals(is_madhav_array([]),False)
        test.assert_equals(is_madhav_array([1]),False)
        test.assert_equals(is_madhav_array([5,2,4,1,0,3]),False)
        test.assert_equals(is_madhav_array([6,2,4,2,2,2,1,5,0,0,-12,13,-5,4,6]),True)
        test.assert_equals(is_madhav_array([6,2,4,2,2,2,1,5,0,0,-12,13,-5,4,1]),False)
        test.assert_equals(is_madhav_array([2,1,1]),True)
        test.assert_equals(is_madhav_array([2,1,1,4,-1,-1]),True)