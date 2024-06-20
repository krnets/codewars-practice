import codewars_test as test
from kata import black_or_white_key

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(black_or_white_key(1), "white")
        test.assert_equals(black_or_white_key(5), "black")
        test.assert_equals(black_or_white_key(12), "black")
        test.assert_equals(black_or_white_key(42), "white")
        test.assert_equals(black_or_white_key(88), "white")
        test.assert_equals(black_or_white_key(89), "white")
        test.assert_equals(black_or_white_key(92), "white")
        test.assert_equals(black_or_white_key(100), "black")
        test.assert_equals(black_or_white_key(111), "white")
        test.assert_equals(black_or_white_key(200), "black")
        test.assert_equals(black_or_white_key(2017), "white")