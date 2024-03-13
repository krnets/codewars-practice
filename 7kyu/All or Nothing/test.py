import codewars_test as test
from kata import possibly_perfect

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Simple Cases')
    def example_cases():
        test.assert_equals(possibly_perfect(['A', '_', 'C', '_', 'B'], ['A', 'D', 'C', 'E', 'B']), True)
        test.assert_equals(possibly_perfect(['B', '_', 'B'], ['B', 'D', 'C']), False)
        test.assert_equals(possibly_perfect(['T', '_', 'F', 'F', 'F'], ['F', 'F', 'T', 'T', 'T']), True)

        test.assert_equals(possibly_perfect(['B', 'A', '_', '_'], ['B', 'A', 'C', 'C']), True)
        test.assert_equals(possibly_perfect(['A', 'B', 'A', '_'], ['B', 'A', 'C', 'C']), True)
        test.assert_equals(possibly_perfect(['A', 'B', 'C', '_'], ['B', 'A', 'C', 'C']), False)

        test.assert_equals(possibly_perfect(['B', '_'], ['C', 'A']), True)
        test.assert_equals(possibly_perfect(['B', 'A'], ['C', 'A']), False)
        test.assert_equals(possibly_perfect(['B'], ['B']), True)

        test.assert_equals(possibly_perfect(['_', 'T', '_', '_'], ['T', 'F', 'F', 'F']), True)
        test.assert_equals(possibly_perfect(['_', 'T', '_', '_'], ['T', 'T', 'F', 'T']), True)
        test.assert_equals(possibly_perfect(['_', 'T', 'T', 'T'], ['T', 'T', 'F', 'T']), False)
        test.assert_equals(possibly_perfect(['_', 'T', 'T', 'T'], ['T', 'T', 'T', 'T']), True)
        test.assert_equals(possibly_perfect(['_', 'T', 'T', 'T'], ['F', 'F', 'F', 'F']), True)
        test.assert_equals(possibly_perfect(['_', '_', '_', '_'], ['F', 'F', 'F', 'F']), True)