import codewars_test as test
from kata import shifted_diff


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(shifted_diff("eecoff", "coffee"), 4)
        test.assert_equals(shifted_diff("Moose", "moose"), -1)
        test.assert_equals(shifted_diff("isn't", "'tisn"), 2)
        test.assert_equals(shifted_diff("Esham", "Esham"), 0)
        test.assert_equals(shifted_diff(" ", " "), 0)
        test.assert_equals(shifted_diff("hoop", "pooh"), -1)
        test.assert_equals(shifted_diff("  ", " "), -1)
