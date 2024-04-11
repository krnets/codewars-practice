import codewars_test as test
from kata import total

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(total([]),0)
        test.assert_equals(total([1,2,3,4]),7)
        test.assert_equals(total([1,2,3,4,5,6]),13)
        test.assert_equals(total([1,2,3,4,5,6,7,8]),21)
        test.assert_equals(total([1,2,3,4,5,6,7,8,9,10,11]),21)
        test.assert_equals(total([1,2,3,4,5,6,7,8,9,10,11,12,13]),33)
        test.assert_equals(total([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]),47)