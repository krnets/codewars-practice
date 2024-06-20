import codewars_test as test
from kata import password_cracker

@test.it('Sample tests')
def tests():
    test.assert_equals(password_cracker('e6fb06210fafc02fd7479ddbed2d042cc3a5155e'), 'code')
    test.assert_equals(password_cracker('a94a8fe5ccb19ba61c4c0873d391e987982fbbd3'), 'test')