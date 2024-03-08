import codewars_test as test
from kata import date_correct

test.describe("Basic tests")
test.it("None or empty")
test.assert_equals(date_correct(None), None)
test.assert_equals(date_correct(""), "")
test.it("Invalid Format")
test.assert_equals(date_correct("01112016"), None)
test.assert_equals(date_correct("01,11,2016"), None)
test.assert_equals(date_correct("0a.1c.2016"), None)
test.it("Correction Tests")
test.assert_equals(date_correct("03.12.2016"), "03.12.2016")
test.assert_equals(date_correct("30.02.2016"), "01.03.2016")
test.assert_equals(date_correct("40.06.2015"), "10.07.2015")
test.assert_equals(date_correct("11.13.2014"), "11.01.2015")
test.assert_equals(date_correct("33.13.2014"), "02.02.2015")
test.assert_equals(date_correct("99.11.2010"), "07.02.2011")
