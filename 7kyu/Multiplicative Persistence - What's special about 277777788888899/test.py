import codewars_test as test
from kata import per

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(per(0), [])
        test.assert_equals(per(2), [])
        test.assert_equals(per(3), [])
        test.assert_equals(per(9), [])
        test.assert_equals(per(1234567890), [0])
        test.assert_equals(per(123456789), [362880, 0])
        test.assert_equals(per(12345678), [40320, 0])
        test.assert_equals(per(1234567), [5040, 0])
        test.assert_equals(per(123456), [720, 0])
        test.assert_equals(per(12345), [120, 0])
        test.assert_equals(per(2379), [378, 168, 48, 32, 6])
        test.assert_equals(per(777), [343, 36, 18, 8])
        test.assert_equals(per(25), [10, 0])
        test.assert_equals(per(277777788888899), [4996238671872, 438939648, 4478976, 338688, 27648, 2688, 768, 336, 54, 20, 0])
        test.assert_equals(per(3778888999), [438939648,  4478976,  338688,  27648,  2688,  768,  336,  54,  20,  0])