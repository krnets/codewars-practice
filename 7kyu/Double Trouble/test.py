import codewars_test as test
from kata import trouble


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        TESTS = [
            # [(input), expected],
            [([1, 3, 5, 6, 7, 4, 3], 7), [1, 3, 5, 6, 7, 4]],
            [([4, 1, 1, 1, 4], 2), [4, 1, 4]],
            [([2, 6, 2], 8), [2, 2]],
            [([2, 2, 2, 2, 2, 2], 4), [2]],
        ]

        for inp, exp in TESTS:
            test.assert_equals(trouble(*inp), exp)
