import codewars_test as test
from kata import lowest_temp

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(lowest_temp(''), None)
        test.assert_equals(lowest_temp('-1 50 -4 20 22 -7 0 10 -8'), -8)