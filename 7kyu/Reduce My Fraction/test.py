import codewars_test as test
from kata import reduce_fraction


@test.describe("Basic Tests")
def _():
    @test.it("Simple Fractions")
    def _():
        test.assert_equals(reduce_fraction((60, 20)), (3, 1))
        test.assert_equals(reduce_fraction((80, 120)), (2, 3))
        test.assert_equals(reduce_fraction((4, 2)), (2, 1))
        test.assert_equals(reduce_fraction((45, 120)), (3, 8))
        test.assert_equals(reduce_fraction((1000, 1)), (1000, 1))
        test.assert_equals(reduce_fraction((1, 1)), (1, 1))
