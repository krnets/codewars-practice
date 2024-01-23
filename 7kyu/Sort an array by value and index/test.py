import codewars_test as test
from kata import sort_by_value_and_index

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sort_by_value_and_index([ 1, 2, 3, 4, 5 ]), [ 1, 2, 3, 4, 5 ])
        test.assert_equals(sort_by_value_and_index([ 23, 2, 3, 4, 5 ]), [ 2, 3, 4, 23, 5 ])
        test.assert_equals(sort_by_value_and_index([ 26, 2, 3, 4, 5 ]), [ 2, 3, 4, 5, 26 ])
        test.assert_equals(sort_by_value_and_index([ 9, 5, 1, 4, 3 ]), [ 1, 9, 5, 3, 4 ])