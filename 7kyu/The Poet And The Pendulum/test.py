import codewars_test as test
from kata import pendulum


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(pendulum([4, 6, 8, 7, 5]), [8, 6, 4, 5, 7])
        test.assert_equals(
            pendulum([19, 30, 16, 19, 28, 26, 28, 17, 21, 17]),
            [28, 26, 19, 17, 16, 17, 19, 21, 28, 30],
        )
        test.assert_equals(pendulum([-9, -2, -10, -6]), [-6, -10, -9, -2])
        test.assert_equals(
            pendulum([-19, -9, -5, -6, -15, -16, -5, -12]),
            [-5, -9, -15, -19, -16, -12, -6, -5],
        )
        test.assert_equals(
            pendulum([11, -16, -18, 13, -11, -12, 3, 18]),
            [13, 3, -12, -18, -16, -11, 11, 18],
        )
