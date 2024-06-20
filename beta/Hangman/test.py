from kata import Hangman
import codewars_test as test

@test.describe("hangman")
def tests():
    @test.it("should return the correct things")
    def test_second_oldest_first():
        test.assert_equals(Hangman('E', 'Hanger'), '____e_')
        test.assert_equals(Hangman('C', 'Coat'), 'c___')
        test.assert_equals(Hangman('U', 'Olive'), '_____')