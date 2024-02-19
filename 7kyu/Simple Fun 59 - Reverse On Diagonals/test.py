import codewars_test as test
from kata import reverse_on_diagonals


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            reverse_on_diagonals([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [[9, 2, 7], [4, 5, 6], [3, 8, 1]],
        )
        test.assert_equals(reverse_on_diagonals([[239]]), [[239]])
        test.assert_equals(
            reverse_on_diagonals([[1, 10], [100, 1000]]), [[1000, 100], [10, 1]]
        )
        test.assert_equals(
            reverse_on_diagonals(
                [
                    [43, 455, 32, 103],
                    [102, 988, 298, 981],
                    [309, 21, 53, 64],
                    [2, 22, 35, 291],
                ]
            ),
            [
                [291, 455, 32, 2],
                [102, 53, 21, 981],
                [309, 298, 988, 64],
                [103, 22, 35, 43],
            ],
        )
