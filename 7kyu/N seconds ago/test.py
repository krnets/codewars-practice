import codewars_test as test
from kata import seconds_ago


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(seconds_ago("2000-01-01 00:00:00", 1), "1999-12-31 23:59:59")
        test.assert_equals(seconds_ago("0001-02-03 04:05:06", 7), "0001-02-03 04:04:59")
