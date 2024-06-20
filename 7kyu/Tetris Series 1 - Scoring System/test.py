import codewars_test as test
from kata import get_score


@test.describe("Fixed tests")
def fixed_tests():

    @test.it("Basic tests")
    def basic_tests():
        test.assert_equals(get_score([0, 1, 2, 3, 4]), 1640)
        test.assert_equals(get_score([0, 1, 1, 3, 0, 2, 1, 2]), 620)
        test.assert_equals(get_score([2, 0, 4, 2, 2, 3, 0, 0, 3, 3]), 3300)

    @test.it("Special tests")
    def special_tests():
        test.assert_equals(get_score([0]), 0)
        test.assert_equals(get_score([]), 0)
