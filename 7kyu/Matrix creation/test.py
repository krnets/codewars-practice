import codewars_test as test
from kata import get_matrix


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(get_matrix(0), [])
        test.assert_equals(get_matrix(1), [[1]])
        test.assert_equals(get_matrix(2), [[1, 0], [0, 1]])
        test.assert_equals(get_matrix(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        test.assert_equals(
            get_matrix(5),
            [
                [1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1],
            ],
        )
