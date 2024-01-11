import codewars_test as test
from kata import unused_digits

@test.describe("Sample Tests")
def basic_tests():
    @test.it("Tests")
    def it_1():
        test.assert_equals(unused_digits(12, 34, 56, 78), "09")
        test.assert_equals(unused_digits(2015, 8, 26), "3479")
        test.assert_equals(unused_digits(276, 575), "013489")
        test.assert_equals(unused_digits(643), "0125789")
        test.assert_equals(unused_digits(864, 896, 744), "01235")