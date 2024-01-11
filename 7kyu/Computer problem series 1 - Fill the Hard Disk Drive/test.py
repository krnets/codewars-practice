import codewars_test as test
from kata import save


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Simple Cases")
    def example_cases():
        test.assert_equals(save([4, 4, 4, 3, 3], 12), 3)
        test.assert_equals(save([4, 4, 4, 3, 3], 11), 2)
        test.assert_equals(save([4, 8, 15, 16, 23, 42], 108), 6)
        test.assert_equals(save([13], 13), 1)
        test.assert_equals(save([1, 2, 3, 4], 250), 4)
        test.assert_equals(save([100], 500), 1)
        test.assert_equals(save([11, 13, 15, 17, 19], 8), 0)
        test.assert_equals(save([45], 12), 0)

        test.assert_equals(save([12, 0, 0, 1], 12), 3)
