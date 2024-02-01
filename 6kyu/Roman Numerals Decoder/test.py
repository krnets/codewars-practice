import codewars_test as test
from kata import solution

@test.describe('Tests')
def tests():

    def do_test(roman : str, n : int):
        actual = solution(roman)
        test.assert_equals(actual, n, f'for roman {roman}')

    @test.it('Sample Tests')
    def sample_tests():
        do_test('MMMCMXCIX',       3999)
        do_test('MMMDCCCLXXXVIII', 3888)
        do_test('MM',              2000)
        do_test('MDCLXVI',         1666)
        do_test('M' ,              1000)
        do_test('CD',               400)
        do_test('XC',                90)
        do_test('XL',                40)
        do_test('I' ,                 1)