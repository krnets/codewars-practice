import codewars_test as test
from kata import ip_to_int32


@test.describe("Basic Tests")
def basic_tests():

    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(ip_to_int32("128.114.17.104"), 2154959208)
        test.assert_equals(ip_to_int32("0.0.0.0"), 0)
        test.assert_equals(ip_to_int32("128.32.10.1"), 2149583361)
