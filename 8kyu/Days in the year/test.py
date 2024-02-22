import codewars_test as test
from kata import year_days

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(year_days(0), '0 has 366 days')
        test.assert_equals(year_days(-64), '-64 has 366 days')
        test.assert_equals(year_days(2016), '2016 has 366 days')
        test.assert_equals(year_days(1974), '1974 has 365 days')
        test.assert_equals(year_days(-10), '-10 has 365 days')
        test.assert_equals(year_days(666), '666 has 365 days')
        test.assert_equals(year_days(1857), '1857 has 365 days')
        test.assert_equals(year_days(2000), '2000 has 366 days')
        test.assert_equals(year_days(-300), '-300 has 365 days')
        test.assert_equals(year_days(-1), '-1 has 365 days')