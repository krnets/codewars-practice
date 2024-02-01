import codewars_test as test
from kata import is_valid_IP


@test.describe("Sample tests")
def _():
    @test.it("Valid IP Tests")
    def __():
        test.assert_equals(is_valid_IP('1.2.3.4'),          True)
        test.assert_equals(is_valid_IP('12.255.56.1'),      True)
        test.assert_equals(is_valid_IP('127.1.1.0'),        True)
        test.assert_equals(is_valid_IP('0.0.0.0'),          True)
        test.assert_equals(is_valid_IP('0.34.82.53'),       True)
        test.assert_equals(is_valid_IP('123.45.67.89'),     True)

    @test.it("Invalid IP Tests")
    def __():
        test.assert_equals(is_valid_IP(''),                False)
        test.assert_equals(is_valid_IP('abc.def.ghi.jkl'), False)
        test.assert_equals(is_valid_IP('123.456.789.0'),   False)
        test.assert_equals(is_valid_IP('123.456.78.90'),   False)
        test.assert_equals(is_valid_IP('12.34.56'),        False)
        test.assert_equals(is_valid_IP('12.34.56 .1'),     False)
        test.assert_equals(is_valid_IP('12.34.56.-1'),     False)
        test.assert_equals(is_valid_IP('123.045.067.089'), False)
        test.assert_equals(is_valid_IP('192.168.1.300'),   False)
        test.assert_equals(is_valid_IP('70.00.87.80'),     False)