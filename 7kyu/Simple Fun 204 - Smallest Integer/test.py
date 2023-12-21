import codewars_test as test
from kata import smallest_integer


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(smallest_integer([[-1, -1], [-1, -1]]), 0)
        test.assert_equals(smallest_integer([[1, 2], [3, 4]]), 0)
        test.assert_equals(smallest_integer([[0, 1], [2, 3]]), 4)
        test.assert_equals(smallest_integer([[0, 2], [5, 1]]), 3)

        test.assert_equals(
            smallest_integer(
                [
                    [4, 5, 3, 21, 3, 8],
                    [2, 2, 6, 5, 10, 9],
                    [7, 5, 6, 8, 2, 6],
                    [1, 4, 7, 8, 9, 0],
                    [1, 3, 6, 5, 5, 1],
                    [2, 7, 3, 4, 4, 3],
                ]
            ),
            11,
        )

        test.assert_equals(
            smallest_integer(
                [
                    [4, 5, 3, -4, 3, 8],
                    [2, 0, 6, 5, 4, 9],
                    [7, 5, 6, 8, 2, 6],
                    [1, 4, 7, 8, 9, 11],
                    [1, 3, 10, 5, 5, 1],
                    [12, 7, 3, 4, 4, 3],
                ]
            ),
            13,
        )

        test.assert_equals(
            smallest_integer(
                [
                    [4, 5, 13, 0, 3],
                    [2, 6, 5, 10, 9],
                    [7, 5, -6, 8, 6],
                    [1, 4, 7, 8, 9],
                    [2, 3, 4, 44, 3],
                ]
            ),
            11,
        )

        test.assert_equals(
            smallest_integer(
                [
                    [-1, 100, -1, 100],
                    [100, -1, 100, -1],
                    [-1, 100, -1, 100],
                    [100, -1, 100, -1],
                ]
            ),
            0,
        )
