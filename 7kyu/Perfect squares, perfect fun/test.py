import codewars_test as test
from kata import square_it

sample_test_cases = [
    (           1, '1'),
    (         222, 'Not a perfect square!'),
    (        1212, '12\n12'),
    (   123123123, '123\n123\n123'),
    (234562342342, 'Not a perfect square!'),
    (       88989, 'Not a perfect square!'),
    (   112141568, '112\n141\n568'),
]

@test.describe('Sample tests')
def sample_tests():
    for n, expected in sample_test_cases:
        @test.it(f'square_it({n})')
        def _():
            test.assert_equals(square_it(n), expected)