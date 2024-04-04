from kata import sum_diagonals
import codewars_test as test


@test.it("Sample tests")
def sample_tests():
    test.assert_equals(
        sum_diagonals([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 1 + 5 + 9 + 3 + 5 + 7
    )
