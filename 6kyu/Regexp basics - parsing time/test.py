import codewars_test as test
from kata import to_seconds


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(to_seconds("00:00:00"), 0)
        test.assert_equals(to_seconds("01:02:03"), 3723)
        test.assert_equals(to_seconds("01:02:60"), None)
        test.assert_equals(to_seconds("01:60:03"), None)
        test.assert_equals(to_seconds("99:59:59"), 359999)
        test.assert_equals(to_seconds("0:00:00"), None)
        test.assert_equals(to_seconds("00:0:00"), None)
        test.assert_equals(to_seconds("00:00:0"), None)
        test.assert_equals(to_seconds("00:00:00\n"), None)
        test.assert_equals(to_seconds("\n00:00:00"), None)
        test.assert_equals(to_seconds("100:59:59"), None)
        test.assert_equals(to_seconds("09:059:59"), None)
        test.assert_equals(to_seconds("09:159:59"), None)
        test.assert_equals(to_seconds("09:59:059"), None)
        test.assert_equals(to_seconds("09:59:159"), None)
