import codewars_test as test
from kata import sum_arrays
from collections import namedtuple


@test.describe("Basic Tests")
def _():

    TestData = namedtuple('TestData', ['arrays', 'shift', 'expected'])

    tests = [
        TestData(
            arrays=[[1, 2, 3, 4, 5, 6], [7, 7, 7, 7, 7, -7]],
            shift=0,
            expected=[8, 9, 10, 11, 12, -1]
        ),
        TestData(
            arrays=[[1, 2, 3, 4, 5, 6], [7, 7, 7, 7, 7, 7 ]],
            shift=3,
            expected=[1, 2, 3, 11, 12, 13, 7, 7, 7]
        ),
        TestData(
            arrays=[[1, 2, 3, 4, 5, 6], [7, 7, 7, -7, 7, 7], [1, 1, 1, 1, 1, 1]],
            shift=3,
            expected=[1, 2, 3, 11, 12, 13, -6, 8, 8, 1, 1, 1]
        )
    ]

    for t in tests:
        @test.it(f'Arrays: {t.arrays}, shift: {t.shift}')
        def _():
            test.assert_equals(sum_arrays(t.arrays, t.shift), t.expected)
