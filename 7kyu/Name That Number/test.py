import codewars_test as test
from kata import name_that_number


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(name_that_number(0), "zero")
        test.assert_equals(name_that_number(4), "four")
        test.assert_equals(name_that_number(9), "nine")
        test.assert_equals(name_that_number(19), "nineteen")
        test.assert_equals(name_that_number(23), "twenty three")
        test.assert_equals(name_that_number(99), "ninety nine")
        test.assert_equals(name_that_number(40), "forty")
