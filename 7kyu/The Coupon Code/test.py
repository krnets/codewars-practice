from kata import check_coupon
import codewars_test as test

@test.it("Example tests")
def example_tests():
    test.assert_equals(check_coupon('123','123','September 5, 2014','October 1, 2014'), True);
    test.assert_equals(check_coupon('123a','123','September 5, 2014','October 1, 2014'), False);