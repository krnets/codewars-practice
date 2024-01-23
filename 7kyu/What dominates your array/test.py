import codewars_test as test
from kata import dominator


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(dominator([3, 4, 3, 2, 3, 1, 3, 3]), 3)
        test.assert_equals(dominator([1, 2, 3, 4, 5]), -1)
        test.assert_equals(dominator([1, 1, 1, 2, 2, 2]), -1)
        test.assert_equals(dominator([1, 1, 1, 2, 2, 2, 2]), 2)
        test.assert_equals(dominator([]), -1)
