import codewars_test as test
from kata import to_binary

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(to_binary(2),"10")
        test.assert_equals(to_binary(3),"11")
        test.assert_equals(to_binary(4),"100")
        test.assert_equals(to_binary(5),"101")
        test.assert_equals(to_binary(7),"111")
        test.assert_equals(to_binary(10),"1010")
        test.assert_equals(to_binary(-3),"11111111111111111111111111111101")
        test.assert_equals(to_binary(0),"0")
        test.assert_equals(to_binary(1000),"1111101000")
        test.assert_equals(to_binary(-15),"11111111111111111111111111110001")
        test.assert_equals(to_binary(-1000),"11111111111111111111110000011000")
        test.assert_equals(to_binary(-999999),"11111111111100001011110111000001")
        test.assert_equals(to_binary(999999),"11110100001000111111")