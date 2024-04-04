import codewars_test as test
from kata import hidden

@test.describe("Basic Tests")
def _():    
    @test.it("Expected '637` to return 'aid'")
    def _():
        test.assert_equals(hidden(637), "aid")
    @test.it("Expected '7415` to return 'debt'")
    def _():
        test.assert_equals(hidden(7415), "debt")
    @test.it("Expected '49632` to return 'email'")
    def _():
        test.assert_equals(hidden(49632), "email")
    @test.it("Expected '942547` to return 'melted'")
    def _():
        test.assert_equals(hidden(942547), "melted");