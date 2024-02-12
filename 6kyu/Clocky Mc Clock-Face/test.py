import codewars_test as test
from kata import what_time_is_it


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(what_time_is_it(0), "12:00")
        test.assert_equals(what_time_is_it(360), "12:00")
        test.assert_equals(what_time_is_it(90), "03:00")
        test.assert_equals(what_time_is_it(180), "06:00")
        test.assert_equals(what_time_is_it(270), "09:00")
        test.assert_equals(what_time_is_it(30), "01:00")
        test.assert_equals(what_time_is_it(22.5263), "12:45")
