import codewars_test as test
from kata import direction

@test.describe("Sample tests")
def tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(direction("S", 180),  "N")
        test.assert_equals(direction("SE", -45), "E")
        test.assert_equals(direction("W", 495),  "NE")