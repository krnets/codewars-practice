import codewars_test as test
from kata import make_readable

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(make_readable(0), "00:00:00")
        test.assert_equals(make_readable(59), "00:00:59")
        test.assert_equals(make_readable(60), "00:01:00")
        test.assert_equals(make_readable(3599), "00:59:59")
        test.assert_equals(make_readable(3600), "01:00:00")
        test.assert_equals(make_readable(86399), "23:59:59")
        test.assert_equals(make_readable(86400), "24:00:00")
        test.assert_equals(make_readable(359999), "99:59:59")