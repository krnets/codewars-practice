import codewars_test as test
from kata import fold_array

sample_test_cases = [
    #             array     runs    expected
    (       [1, 2, 3, 4, 5],  1,    [6, 6, 3]),
    (       [1, 2, 3, 4, 5],  2,    [9, 6]),
    (       [1, 2, 3, 4, 5],  3,    [15]),
    ([-9, 9, -8, 8, 66, 23],  1,    [14, 75, 0]),
]

@test.describe('Sample tests')
def sample_tests():
    for orig_array, runs, expected in sample_test_cases:
        @test.it(f'fold_array({orig_array}, {runs})')
        def _():
            array = orig_array.copy()
            actual = fold_array(array, runs)
            if array == orig_array:
                test.assert_equals(actual, expected)
            else:
                test.fail('The input array should not be modified')