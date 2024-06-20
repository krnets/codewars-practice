import codewars_test as test
from kata import even_fib

sample_test_cases = [
    ( 1,   0),
    ( 2,   0),
    ( 3,   2),
    ( 5,   2),
    ( 8,   2),
    (10,  10),
    (33,  10),
    
    (25_997_544, 19_544_084),
]

@test.describe('Sample tests')
def sample_tests():
    for n, expected in sample_test_cases:
        @test.it(f'even_fib({n:_})')
        def _():
            test.assert_equals(even_fib(n), expected)