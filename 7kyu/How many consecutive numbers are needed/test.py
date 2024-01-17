import codewars_test as test
from kata import consecutive


@test.describe("Basic Tests")
def basic_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(consecutive([4, 8, 6]), 2)
        test.assert_equals(consecutive([1, 2, 3, 4]), 0)
        test.assert_equals(consecutive([]), 0)
        test.assert_equals(consecutive([1]), 0)
        test.assert_equals(consecutive([-10]), 0)
        test.assert_equals(consecutive([1, -1]), 1)
        test.assert_equals(consecutive([-10, -9]), 0)
        test.assert_equals(consecutive([0]), 0)
        test.assert_equals(consecutive([10, -10]), 19)
        test.assert_equals(consecutive([-10, 10]), 19)
