import codewars_test as test
from kata import rpsls


@test.describe('rock paper scissors lizard spock')
def test():
    @test.it('Player 1 Won!')
    def _():
        test.assert_equals(rpsls('rock', 'lizard'), 'Player 1 Won!')
        test.assert_equals(rpsls('paper', 'rock'), 'Player 1 Won!')
        test.assert_equals(rpsls('scissors', 'lizard'), 'Player 1 Won!')
        test.assert_equals(rpsls('lizard', 'paper'), 'Player 1 Won!')
        test.assert_equals(rpsls('spock', 'rock'), 'Player 1 Won!')
    
    @test.it('Player 2 Won!')
    def _():
        test.assert_equals(rpsls('lizard','scissors'), 'Player 2 Won!')
        test.assert_equals(rpsls('spock','lizard'), 'Player 2 Won!')
        test.assert_equals(rpsls('paper','lizard'), 'Player 2 Won!')
        test.assert_equals(rpsls('scissors','spock'), 'Player 2 Won!')
        test.assert_equals(rpsls('rock','spock'), 'Player 2 Won!')
    
    @test.it("Draw!")
    def _():
        test.assert_equals(rpsls('rock', 'rock'), 'Draw!')
        test.assert_equals(rpsls('spock', 'spock'), 'Draw!')
