import codewars_test as test
from kata import triangular

sample_test_cases = [
    (  0,  0),
    (  1,  1),
    (  2,  3),
    (  3,  6),
    (  4, 10),
    (  5, 15),
    (  6, 21),
    (  7, 28),
    (  8, 36),
    (  9, 45),
    (  10, 55),
    (  11, 66),
    (  12, 78),
    (  13, 91),
    (  14, 105),
    (-10,  0),
]

@test.describe('Sample tests')
def sample_tests():
    for n, expected in sample_test_cases:
        @test.it(f'triangular({n})')
        def _():
            test.assert_equals(triangular(n), expected)