import codewars_test as test
from kata import ipv4_address

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(ipv4_address(""), False)
        test.assert_equals(ipv4_address("127.0.0.1"), True)
        test.assert_equals(ipv4_address("0.0.0.0"), True)
        test.assert_equals(ipv4_address("255.255.255.255"), True)
        test.assert_equals(ipv4_address("10.20.30.40"), True)
        test.assert_equals(ipv4_address("10.256.30.40"), False)
        test.assert_equals(ipv4_address("10.20.030.40"), False)
        test.assert_equals(ipv4_address("127.0.1"), False)
        test.assert_equals(ipv4_address("127.0.0.0.1"), False)
        test.assert_equals(ipv4_address("..255.255"), False)
        test.assert_equals(ipv4_address("127.0.0.1\n"), False)
        test.assert_equals(ipv4_address("\n127.0.0.1"), False)
        test.assert_equals(ipv4_address(" 127.0.0.1"), False)
        test.assert_equals(ipv4_address("127.0.0.1 "), False)
        test.assert_equals(ipv4_address(" 127.0.0.1 "), False)
        test.assert_equals(ipv4_address("127.0.0.1."), False)
        test.assert_equals(ipv4_address(".127.0.0.1"), False)
        test.assert_equals(ipv4_address("127..0.1"), False)