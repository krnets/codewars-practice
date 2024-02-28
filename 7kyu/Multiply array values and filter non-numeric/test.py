import codewars_test as test
from kata import multiply_and_filter

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(multiply_and_filter([1,2,3,4], 1.5), [1.5, 3, 4.5, 6])
    test.assert_equals(multiply_and_filter([1,2,3], 0), [0, 0, 0])
    test.assert_equals(multiply_and_filter([0,0,0], 2), [0, 0, 0])
    test.assert_equals(multiply_and_filter([1, None, lambda x: x, 2.5, 'string', 10, None, {}, []], 3), [3,7.5,30])
    test.assert_equals(multiply_and_filter([1, None, lambda x: x, 2.5, 'string', 10, None, {}, [], True, False], 3), [3,7.5,30])
