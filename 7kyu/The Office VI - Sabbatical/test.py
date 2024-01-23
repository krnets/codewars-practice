import codewars_test as test
from kata import sabb

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sabb("Can I have a sabbatical?", 5, 5), "Sabbatical! Boom!")
        test.assert_equals(sabb("Why are you shouting?", 7, 2), "Back to your desk, boy.")
        test.assert_equals(sabb("What do you mean I cant learn to code??", 8, 9), "Sabbatical! Boom!")
        test.assert_equals(sabb("Please calm down", 9, 1), "Back to your desk, boy.")