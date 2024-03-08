import codewars_test as test
from kata import convert_temp

test.assert_equals(convert_temp(100, "C", "F"), 212)
test.assert_equals(convert_temp(-30, "De", "K"), 393)
test.assert_equals(convert_temp(40, "Re", "C"), 50)
test.assert_equals(convert_temp(60, "De", "F"), 140)
test.assert_equals(convert_temp(373.15, "K", "N"), 33)
test.assert_equals(convert_temp(666, "K", "K"), 666)
