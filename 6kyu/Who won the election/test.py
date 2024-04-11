from kata import get_winner
import codewars_test as test

@test.describe("Who won this election")
def desc():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(get_winner(("A")), "A")
        test.assert_equals(get_winner(("A", "A", "A", "B", "B", "B", "A")), "A")
        test.assert_equals(get_winner(("A", "A", "A", "B", "B", "B")), None)
        test.assert_equals(get_winner(("A", "A", "A", "B", "C", "B")), None)
        test.assert_equals(get_winner(("A", "A", "B", "B", "C")), None)   