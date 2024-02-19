import codewars_test as test
from kata import any_odd


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(any_odd(2863311530), True)
        test.assert_equals(any_odd(128), True)
        test.assert_equals(any_odd(131), True)
        test.assert_equals(any_odd(2), True)
        test.assert_equals(any_odd(24082), True)
        test.assert_equals(any_odd(0), False)
        test.assert_equals(any_odd(85), False)
        test.assert_equals(any_odd(1024), False)
        test.assert_equals(any_odd(1), False)
        test.assert_equals(any_odd(1365), False)
        test.assert_equals(any_odd(8606990356), False)
        test.assert_equals(any_odd(8674869588), False)
        test.assert_equals(any_odd(8880455745), False)
        test.assert_equals(any_odd(9664794625), False)
        test.assert_equals(any_odd(8657126737), False)
