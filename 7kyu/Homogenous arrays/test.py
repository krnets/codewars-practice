import codewars_test as test
from kata import filter_homogenous

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(filter_homogenous([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]), [[1, 5, 4], ['b']])
        test.assert_equals(filter_homogenous([[123, 234, 432], ['', 'abc'], [''], ['', 1], ['', '1'], []]), [[123, 234, 432], ['', 'abc'], [''], ['', '1']])
        test.assert_equals(filter_homogenous([[1, 2, 3], ["1", "2", "3"], ["1", 2, 3]]), [[1, 2, 3], ["1", "2", "3"]])