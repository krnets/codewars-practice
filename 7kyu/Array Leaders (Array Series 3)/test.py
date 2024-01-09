import codewars_test as test
from kata import array_leaders


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Positive Values")
    def positive_values_tests():
        test.assert_equals(array_leaders([1, 2, 3, 4, 0]), [4])
        test.assert_equals(array_leaders([16, 17, 4, 3, 5, 2]), [17, 5, 2])

    @test.it("Negative Values")
    def negative_values_tests():
        test.assert_equals(array_leaders([-1, -29, -26, -2]), [-1])
        test.assert_equals(array_leaders([-36, -12, -27]), [-36, -12])

    @test.it("Mixed Values")
    def negative_values_tests():
        test.assert_equals(array_leaders([5, 2]), [5, 2])
        test.assert_equals(array_leaders([0, -1, -29, 3, 2]), [0, -1, 3, 2])
