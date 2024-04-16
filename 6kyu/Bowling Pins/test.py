from kata import bowling_pins
import codewars_test as test

@test.describe('tests suite')
def tests():

    def do_test(input, expected):
        actual = bowling_pins(input.copy())
        test.assert_equals(actual, expected, f'for {repr(input)}\n')

    @test.it('sample tests')
    def sample_tests():
        do_test([2, 3], "I I I I\n I I I \n       \n   I   ")
        do_test([1, 2, 10], "I I I  \n I I I \n    I  \n       ")