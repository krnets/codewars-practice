import codewars_test as test
from kata import hex_color

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(hex_color(''), 'black')
        test.assert_equals(hex_color('000 000 000'), 'black')
        test.assert_equals(hex_color('121 245 255'), 'blue')
        test.assert_equals(hex_color('027 100 100'), 'cyan')
        test.assert_equals(hex_color('021 021 021'), 'white')
        test.assert_equals(hex_color('255 000 000'), 'red')
        test.assert_equals(hex_color('000 147 000'), 'green')
        test.assert_equals(hex_color('212 103 212'), 'magenta')
        test.assert_equals(hex_color('101 101 092'), 'yellow')