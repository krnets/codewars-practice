import codewars_test as test
from kata import max_ball
    
@test.describe("max_ball")
def tests():
    @test.it("Fixed tests")
    def basics():
        test.assert_equals(max_ball(37), 10)
        test.assert_equals(max_ball(45), 13)
        test.assert_equals(max_ball(99), 28)
        test.assert_equals(max_ball(85), 24)