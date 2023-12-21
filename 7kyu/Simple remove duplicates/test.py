import codewars_test as test
from kata import solve


@test.describe("Basic Tests")
def basic_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(solve([3, 4, 4, 3, 6, 3]), [4, 6, 3])
        test.assert_equals(solve([1, 2, 1, 2, 1, 2, 3]), [1, 2, 3])
        test.assert_equals(solve([1, 2, 3, 4]), [1, 2, 3, 4])
        test.assert_equals(solve([1, 1, 4, 5, 1, 2, 1]), [4, 5, 2, 1])
