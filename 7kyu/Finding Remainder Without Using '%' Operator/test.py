import codewars_test as test
from kata import remainder

@test.describe("Sample Tests:")
def basic():
    @test.it("Basic Tests:")
    def _():
        test.assert_equals(remainder(3,2), 1)
        test.assert_equals(remainder(19,2), 1)
        test.assert_equals(remainder(10,2), 0)
        test.assert_equals(remainder(34,7), 6)
        test.assert_equals(remainder(27,5), 2)