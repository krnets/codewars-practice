import codewars_test as test
from kata import closest

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('simple tests')
    def basic_test_cases():
        test.assert_equals(closest([10, 3, 9, 1]), 1)
        test.assert_equals(closest([2, 4, -1, -3]), -1)
        test.assert_equals(closest([5, 2, -2]), None)
        test.assert_equals(closest([5, 2, 2]), 2)
        test.assert_equals(closest([13, 0, -6]), 0)
        test.assert_equals(closest([1]), 1)

    @test.it('should return None for doubles')
    def basic_test_cases():
        test.assert_equals(closest([5, 1, -1, 2, -10]), None)

    @test.it("should not return None for non-doubles :)")
    def basic_test_cases():
        test.assert_equals(closest([5, -5, -2, 5, -3]), -2)

    @test.it("extra tests")
    def basic_test_cases():
        test.assert_equals(closest([27, 37, 48, -18, 42, 16, 5, 34, 35, 26, -34, 3, -43, 35, 0, -45, -7, 45, 34, -18, 44, 12, 6, -45, 33, 27, -2, 28, 12, 9]), 0)
        test.assert_equals(closest([11, -30, -18, 4, -13, 43, 12, -5, -6, -3, 48, 24, -35, 13, -14, 16, 40, -5, 33, -39, -29, 19, -19, -36, 17, 26, 43, 11, 28, -32]), -3)
        test.assert_equals(closest([28, -36, 49, 39, -33, 22, -5, 23, -24, 47, -47, -30, -20, -18, 40, -21, -45, 10, -48, -26, -12, -21, 48, 16, 26, 21, -9, 33, 8, -49]), -5)
        test.assert_equals(closest([32, -26, 15, 17, -11, -14, 17, 44, 16, 49, 14, 11, 40, 27, -32, 6, 18, 38, 48, -28, -29, -28, 21, -38, 26, -37, -43, 16, 13, -6]), None)
        test.assert_equals(closest([36, 43, 44, -15, 37, 38, -11, 37, 21, 8, 20, -13, -32, -15, 31, -6, -33, -6, -47, 0, 0, 33, 42, 0, -47, -29, -38, 18, -32, -33]), 0)
        test.assert_equals(closest([20, 26, 13, -47, -35, 39, 24, 46, -16, 5, 46, -30, -33, -38, -47, 23, 10, -39, -36, 41, 5, -24, 28, -30, 40, -24, -28, -17, -36, 41]), 5)