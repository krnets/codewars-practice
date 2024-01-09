import codewars_test as test
from kata import Guesser

test.describe('Basic tests')
test.it('Correct guess should return true')
guesser = Guesser(10, 2)
guesser.guess(10)
guesser.guess(10)
guesser.guess(10)
guesser.guess(10)
test.assert_equals(guesser.guess(10), True)

test.it('Wrong guess should return false')
guesser = Guesser(10, 2)
guesser.guess(1)
test.assert_equals(guesser.guess(1),False)

test.it('Lives ran out should throw')
guesser = Guesser(10, 2)
guesser.guess(1)
guesser.guess(2)
    
test.expect_error('Expect error: "Omae wa mo shindeiru"', lambda : guesser.guess(10))