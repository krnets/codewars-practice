import codewars_test as test
from kata import calculate_string

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(calculate_string(";$%§fsdfsd235??df/sdfgf5gh.000kk0000"), "47")
        test.assert_equals(calculate_string("sdfsd23454sdf*2342"), "54929268")
        test.assert_equals(calculate_string("fsdfsd235???34.4554s4234df-sdfgf2g3h4j442"), "-210908")
        test.assert_equals(calculate_string("fsdfsd234.4554s4234df+sf234442"), "234676")
        test.assert_equals(calculate_string("a1a2b3c.c0c/a1a0b.cc00c"), '12')