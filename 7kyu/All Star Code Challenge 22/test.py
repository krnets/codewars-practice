import codewars_test as test
from kata import to_time


@test.describe("Testing toTime() function")
def basic_tests():
    @test.it("Should properly work with example test cases")
    def basic():
        test.assert_equals(to_time(3600), "1 hour(s) and 0 minute(s)")
        test.assert_equals(to_time(3601), "1 hour(s) and 0 minute(s)")
        test.assert_equals(to_time(3500), "0 hour(s) and 58 minute(s)")
        test.assert_equals(to_time(323500), "89 hour(s) and 51 minute(s)")
        test.assert_equals(to_time(0), "0 hour(s) and 0 minute(s)")
