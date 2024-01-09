import codewars_test as test
from kata import pattern


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(pattern(1), "1")
        test.assert_equals(pattern(2), "21\n2")
        test.assert_equals(pattern(5), "54321\n5432\n543\n54\n5")
        test.assert_equals(pattern(0), "")
        test.assert_equals(pattern(-25), "")
