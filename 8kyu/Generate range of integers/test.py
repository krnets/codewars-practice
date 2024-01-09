from solution import generate_link
import codewars_test as test


def gen_test_case(inp, res):
    test.assert_equals(generate_link(inp), res, inp)


test.describe("Basic Tests")

gen_test_case('matt c', 'http://www.codewars.com/users/matt%20c')
gen_test_case('g964', 'http://www.codewars.com/users/g964')
gen_test_case('GiacomoSorbi', 'http://www.codewars.com/users/GiacomoSorbi')
gen_test_case('ZozoFouchtra', 'http://www.codewars.com/users/ZozoFouchtra')
gen_test_case('colbydauph', 'http://www.codewars.com/users/colbydauph')

gen_test_case('g;`q5,\<)p+/zlty*$o:]_7k',
              'http://www.codewars.com/users/g%3B%60q5%2C%5C%3C%29p%2B/zlty%2A%24o%3A%5D_7k')
