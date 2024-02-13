import codewars_test as test
from kata import step

@test.describe("Step")
def _():
    @test.it("Basic tests")
    def _():
        test.assert_equals(step(2,100,110), [101, 103])
        test.assert_equals(step(4,100,110), [103, 107])
        test.assert_equals(step(2,5,5), None)
        test.assert_equals(step(6,100,110), [101, 107])
        test.assert_equals(step(8,300,400), [359, 367])
        test.assert_equals(step(10,300,400), [307, 317])
