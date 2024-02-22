import codewars_test as test
from kata import get_two_complement_int

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(get_two_complement_int(45), 19)
        test.assert_equals(get_two_complement_int(22), 10)
        test.assert_equals(get_two_complement_int(31), 1)
        test.assert_equals(get_two_complement_int(84), 44)
        test.assert_equals(get_two_complement_int(453), 59)
        test.assert_equals(get_two_complement_int(1001), 23)
        test.assert_equals(get_two_complement_int(10), 6)
        test.assert_equals(get_two_complement_int(1), 1)
        test.assert_equals(get_two_complement_int(2), 2)
        test.assert_equals(get_two_complement_int(3), 1)