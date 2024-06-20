import codewars_test as test
from kata import is_odd_heavy

@test.describe("Sample tests")
def sample_tests():
    cases = [
        ([0, 2, 19, 4, 4], True),
        ([1, -2, -1, 2], False),
        ([-3, 2, 1, 3, -1, -2], False),
        ([3, 4, -2, -3, -2], False),
        ([-1, 1, -2, 2, -2, -2, -4, 4], False),
        ([-1, -2, 21], True),
        ([0, 0, 0, 0], False),
        ([0, -1, 1], False),
        ([0, 2, 3], True),
        ([0], False),
        ([], False),
        ([1], True),
        ([0, 1, 2, 3, 4, 0, -2, -1, -4, -3], False),
        ([1, -1, 3, -1], True),
        ([1, -1, 2, -2, 3, -3, 0], False),
        ([3], True),
        ([2, 4, 6], False),
        ([-2, -4, -6, -8, -11], False),
    ]
    
    for xs, expected in cases:
        @test.it(f"Testing {xs}")
        def _():
            test.assert_equals(is_odd_heavy(xs), expected)