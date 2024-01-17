from kata import number_joy
import codewars_test as test


@test.describe("Basic tests")
def test_group():
    test.assert_equals(number_joy(1997), False, "Not a Harshad number")
    test.assert_equals(
        number_joy(1998),
        False,
        "Harshad but digit sum=27, and 27x72 does not equal 1998",
    )
    test.assert_equals(
        number_joy(1729), True, "Harshad and digit sum=19, and 19x91 = 1729"
    )
    test.assert_equals(
        number_joy(18), False, "Harshad but digit sum=9, and 9x9 does not equal 18"
    )
