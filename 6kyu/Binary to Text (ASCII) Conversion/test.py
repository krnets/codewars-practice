from kata import binary_to_string
import codewars_test as test


@test.it("Basic tests")
def basic_tests():
    test.assert_equals(
        binary_to_string("0100100001100101011011000110110001101111"), "Hello"
    )
    test.assert_equals(binary_to_string("00110001001100000011000100110001"), "1011")
