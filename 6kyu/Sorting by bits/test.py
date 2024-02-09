import codewars_test as test
from kata import sort_by_bit


@test.describe("Test: Sorting by bits")
def _():
    @test.it("Test")
    def _():
        a = [7, 6, 15, 8]
        sort_by_bit(a)
        test.assert_equals(a, [8, 6, 7, 15], "Wrong")

        b = [9, 4, 5, 3, 5, 7, 2, 56, 8, 2, 6, 8, 0]
        sort_by_bit(b)
        test.assert_equals(b, [0, 2, 2, 4, 8, 8, 3, 5, 5, 6, 9, 7, 56], "Wrong")

        c = [3, 8, 3, 6, 5, 7, 9, 1]
        sort_by_bit(a)
        test.assert_equals(c, [1, 8, 3, 3, 5, 6, 9, 7], "Wrong")
