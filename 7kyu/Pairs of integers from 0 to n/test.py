import codewars_test as test
from kata import generate_pairs

@test.describe("Pairs of integers from 0 to n")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(generate_pairs(2), [[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2]])
        test.assert_equals(generate_pairs(0), [[0, 0]])