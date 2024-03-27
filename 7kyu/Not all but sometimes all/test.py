import codewars_test as test
from kata import binary_cleaner

@test.describe('Example Tests')
def example_tests():        
    test.assert_equals(binary_cleaner([0,1,2,1,0,2,1,1,1,0,4,5,6,2,1,1,0]), ( [ 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0 ], [ 2, 5, 10, 11, 12, 13 ] ))
    test.assert_equals(binary_cleaner([0,1,1,2,0]), ( [ 0, 1, 1, 0 ], [ 3 ] ))
    test.assert_equals(binary_cleaner([2,2,0]), ( [ 0 ], [ 0, 1 ] ))
    test.assert_equals(binary_cleaner([0,1,2,1,0,2,1,1]), ( [ 0, 1, 1, 0, 1, 1 ], [ 2, 5 ] ))
    test.assert_equals(binary_cleaner([1]), ( [ 1 ], [] ))