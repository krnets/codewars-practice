import codewars_test as test
from kata import count_salutes


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(count_salutes('>--->---<--<'), 8)
        test.assert_equals(count_salutes('<----<---<-->'), 0)
        test.assert_equals(count_salutes('>-<->-<'), 6)
