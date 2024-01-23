import codewars_test as test
from kata import mirror

fixed_cases = iter(
    [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2, 1]),
        ([1, 3, 2], [1, 2, 3, 2, 1]),
        ([-8, 42, 18, 0, -16], [-16, -8, 0, 18, 42, 18, 0, -8, -16]),
        ([-3, 15, 8, -1, 7, -1], [-3, -1, -1, 7, 8, 15, 8, 7, -1, -1, -3]),
        ([-5, 10, 8, 10, 2, -3, 10], [-5, -3, 2, 8, 10, 10, 10, 10, 10, 8, 2, -3, -5]),
    ]
)


@test.describe("Fixed tests")
def fixed():
    for input, expected in fixed_cases:
        test.assert_equals(mirror(input), expected)
