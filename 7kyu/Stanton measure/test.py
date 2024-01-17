import codewars_test as test
from kata import stanton_measure


@test.describe("Fixed Tests")
def basic_tests():
    test.assert_equals(stanton_measure([1, 4, 3, 2, 1, 2, 3, 2]), 3)
    test.assert_equals(stanton_measure([1, 4, 1, 2, 11, 2, 3, 1]), 1)
