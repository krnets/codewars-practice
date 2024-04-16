import codewars_test as test
from kata import ones_counter

@test.describe("Fixed Tests")
def _():
    @test.it("Tests")
    def _():
        test.assert_equals(ones_counter([0]), [])
        test.assert_equals(ones_counter([1, 0, 1, 1]), [1, 2])
        test.assert_equals(ones_counter([0, 0, 0, 0, 0, 0, 0, 0]), [])
        test.assert_equals(ones_counter([1,1,1,1,1]), [5])
        test.assert_equals(ones_counter([1, 1, 1, 0, 0, 1, 0, 1, 1, 0]), [3, 1, 2])
        test.assert_equals(ones_counter([0, 0, 0, 1, 0, 0, 1, 1]), [1, 2])
        test.assert_equals(ones_counter([1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1]), [1, 2, 4, 1])