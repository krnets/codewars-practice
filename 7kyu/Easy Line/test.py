import codewars_test as test
from kata import easyline

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(easyline(0), 1)
        test.assert_equals(easyline(1), 2)
        test.assert_equals(easyline(4), 70)
        test.assert_equals(easyline(7), 3432)
        test.assert_equals(easyline(13), 10400600)
        test.assert_equals(easyline(17), 2333606220)
        test.assert_equals(easyline(19), 35345263800)
        test.assert_equals(easyline(50), 100891344545564193334812497256)