import codewars_test as test
from kata import split_integer
    
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(split_integer(10, 1), [10])
        test.assert_equals(split_integer(2, 2), [1, 1])
        test.assert_equals(split_integer(20, 5), [4, 4, 4, 4, 4])
        test.assert_equals(split_integer(20, 6), [3,3,3,3,4,4])
        test.assert_equals(split_integer(11, 3), [3,4,4])
        test.assert_equals(split_integer(4000,37),[108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,109,109,109,109])