import codewars_test as test
from kata import step_through_with

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(step_through_with("moon"), True, "You can take the moon, but not the sun")
        test.assert_equals(step_through_with("test"), False, "You can take a challenge, but not a test")
        test.assert_equals(step_through_with("glasses"), True, "You can take your glasses, but not your contacts")
        test.assert_equals(step_through_with("airplane"), False, "You can take a balloon, but not an airplane")
        test.assert_equals(step_through_with("free"), True, "You can be free, but not in chains")
        test.assert_equals(step_through_with("branch"), False, "You can take the tree or the wood, but not a branch")
        test.assert_equals(step_through_with("aardvark"), True, "You can take an aardvark, but not an anteater")