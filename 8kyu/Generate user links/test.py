import codewars_test as test
from kata import generate_link

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        def gen_test_case(inp, res):
            test.assert_equals(generate_link(inp), res, inp)
        gen_test_case('matt c', 'http://www.codewars.com/users/matt%20c')
        gen_test_case('g964', 'http://www.codewars.com/users/g964')
        gen_test_case('GiacomoSorbi', 'http://www.codewars.com/users/GiacomoSorbi')
        gen_test_case('ZozoFouchtra', 'http://www.codewars.com/users/ZozoFouchtra')
        gen_test_case('colbydauph', 'http://www.codewars.com/users/colbydauph')
        gen_test_case('o6{d:&', 'http://www.codewars.com/users/o6%7Bd%3A%26')
        gen_test_case('1p|t{$~+/g(', 'http://www.codewars.com/users/1p%7Ct%7B%24~%2B/g%28')
        gen_test_case('i%]twr)2by_?,;c^({dmf>_z6&/j', 'http://www.codewars.com/users/i%25%5Dtwr%292by_%3F%2C%3Bc%5E%28%7Bdmf%3E_z6%26/j')

