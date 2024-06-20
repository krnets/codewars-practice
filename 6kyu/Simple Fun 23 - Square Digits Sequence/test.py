import codewars_test as test
from kata import square_digits_sequence

sample_test_cases = [
    ( 16,  9),
    (103,  4),
    (  1,  2),
    ( 86,  4),
    (  6, 18),
]

@test.describe('Sample tests')
def sample_tests():
    for n, expected in sample_test_cases:
        @test.it(f'n = {n}')
        def _():
            test.assert_equals(square_digits_sequence(n), expected)