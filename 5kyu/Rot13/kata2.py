import codewars_test as test
from string import ascii_lowercase as abc


def rot13(message):
    abc13 = abc[13:] + abc[:13]
    return message.translate(str.maketrans(abc + abc.upper(), abc13 + abc13.upper()))


@test.describe("Fixed tests")
def tests():

    @test.it("Should obtain correct Rot13 encoding on fixed strings")
    def test_rot13_fixed_strings():
        test.assert_equals(
            rot13("test"), "grfg", "Returned solution incorrect for fixed string = test"
        )
        test.assert_equals(
            rot13("Test"), "Grfg", "Returned solution incorrect for fixed string = Test"
        )
        test.assert_equals(
            rot13("aA bB zZ 1234 *!?%"),
            "nN oO mM 1234 *!?%",
            "Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%",
        )
