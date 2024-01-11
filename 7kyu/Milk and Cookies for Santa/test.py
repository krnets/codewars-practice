from datetime import date
import codewars_test as test
from kata import time_for_milk_and_cookies

test.assert_equals(time_for_milk_and_cookies(date(2013, 12, 24)), True)
test.assert_equals(time_for_milk_and_cookies(date(2013, 10, 24)), False)
test.assert_equals(time_for_milk_and_cookies(date(3000, 12, 24)), True)
