import codewars_test as test
from kata import main_diagonal_product


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        res1 = main_diagonal_product([[1, 0], [0, 1]])
        res2 = main_diagonal_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        test.assert_equals(res1, 1)
        test.assert_equals(res2, 45)
