import codewars_test as test
from kata import solve

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(solve("abba"),"OK")
        test.assert_equals(solve("abbaa"),"remove one")
        test.assert_equals(solve("abbaab"),"not possible")
        test.assert_equals(solve("madmam"),"remove one")
        test.assert_equals(solve("raydarm"),"not possible")
        test.assert_equals(solve("hannah"),"OK")