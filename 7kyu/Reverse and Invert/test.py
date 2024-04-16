import codewars_test as test
from kata import reverse_invert

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_invert([1,2,3,4,5]), [-1,-2,-3,-4,-5])
        test.assert_equals(reverse_invert([-10]), [1])
        test.assert_equals(reverse_invert([-9,-18,99]), [9,81,-99])
        test.assert_equals(reverse_invert([1,12,'a',3.4,87,99.9,-42,50,5.6]),[-1,-21,-78,24,-5])
        test.assert_equals(reverse_invert([]), [])