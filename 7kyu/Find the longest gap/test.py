import codewars_test as test
from kata import gap


@test.describe("Fixed Tests")
def basic_tests():
    test.assert_equals(gap(9), 2)
    test.assert_equals(gap(529), 4)
    test.assert_equals(gap(20), 1)
    test.assert_equals(gap(15), 0)
    test.assert_equals(gap(4493550), 4)
    test.assert_equals(gap(88668), 2)
    test.assert_equals(gap(99792920738741092200), 3)
    test.assert_equals(gap(41), 2)
    test.assert_equals(gap(36633925210), 4)
    test.assert_equals(gap(48389667664697791), 5)
