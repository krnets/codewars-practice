import codewars_test as test
from kata import solve


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_tests():
        test.assert_equals(solve(6, 3), (3, 3))
        test.assert_equals(solve(8, 2), (2, 6))
        test.assert_equals(solve(10, 3), -1)
        test.assert_equals(solve(12, 4), (4, 8))
        test.assert_equals(solve(12, 5), -1)
