import codewars_test as test
from kata import split_and_add

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(split_and_add([1,2,3,4,5], 2), [5,10])
        test.assert_equals(split_and_add([1,2,3,4,5], 3), [15])
        test.assert_equals(split_and_add([15], 3), [15])
        test.assert_equals(split_and_add([32,45,43,23,54,23,54,34], 2), [183, 125])
        test.assert_equals(split_and_add([32,45,43,23,54,23,54,34], 0), [32,45,43,23,54,23,54,34])
        test.assert_equals(split_and_add([3,234,25,345,45,34,234,235,345], 3), [305, 1195])
        test.assert_equals(split_and_add([3,234,25,345,45,34,234,235,345,34,534,45,645,645,645,4656,45,3], 4), [1040, 7712])
        test.assert_equals(split_and_add([23,345,345,345,34536,567,568,6,34536,54,7546,456], 20), [79327])