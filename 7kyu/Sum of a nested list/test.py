import codewars_test as test
from kata import sum_nested

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Should handle non-nested lists')
    def basic_test_cases():
        test.assert_equals(sum_nested([1]), 1)
        test.assert_equals(sum_nested([1, 2, 3, 4]), 10)
        test.assert_equals(sum_nested(list(range(11))), 55)
        
    @test.it('Non-nested edge case')
    def basic_test_cases():
        test.assert_equals(sum_nested([]), 0)

    @test.it('Should handle simple nestings')
    def basic_test_cases():
        test.assert_equals(sum_nested([[1], []]), 1)
        test.assert_equals(sum_nested([[1, 2, 3, 4]]), 10)

    @test.it('Simple nesting edge case')
    def basic_test_cases():
        test.assert_equals(sum_nested([[], []]), 0)

    @test.it('Should handle more complex nestings')
    def basic_test_cases():
        test.assert_equals(sum_nested([1, [1], [[1]], [[[1]]]]), 4)
        test.assert_equals(sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]]), 8)

    @test.it('Complex nesting edge case')
    def basic_test_cases():
        test.assert_equals(sum_nested([[[[], [], [[[[[[[[[[]]]]]]]]]]], [], [], [[[], [[]]]]], []]), 0)