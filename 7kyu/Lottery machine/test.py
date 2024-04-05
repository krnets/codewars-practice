import codewars_test as test
from kata import lottery

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(lottery("wQ8Hy0y5m5oshQPeRCkG"), "805")
        test.assert_equals(lottery("ffaQtaRFKeGIIBIcSJtg"), "One more run!")
        test.assert_equals(lottery("555"), "5")
        test.assert_equals(lottery("HappyNewYear2020"), "20")
        test.assert_equals(lottery("20191224isXmas"), "20194")
        test.assert_equals(lottery(""), "One more run!")