import codewars_test as test
from kata import crossover

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(crossover("110", "001", 2), ["111", "000"])
        test.assert_equals(crossover("111000", "000110", 3), ["111110", "000000"])