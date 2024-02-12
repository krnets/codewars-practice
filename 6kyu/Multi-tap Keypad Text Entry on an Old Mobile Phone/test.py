from kata import presses
import codewars_test as test


@test.describe("Multi-tap keypad text")
def _():
    @test.it("Sample tests")
    def it():
        test.assert_equals(presses("lol"), 9)
        test.assert_equals(presses("LOL"), 9)
        test.assert_equals(presses("HOW R U"), 13)
        test.assert_equals(presses("abcdefghijklmnopqrstuvwxyz"), 56)
        test.assert_equals(presses("0123456789"), 37)
        test.assert_equals(presses("WHERE DO U WANT 2 MEET L8R"), 47)
        test.assert_equals(presses("# *"), 3)
        test.assert_equals(presses("0"), 2)
        test.assert_equals(presses("ZER0"), 11)
        test.assert_equals(presses("IS NE1 OUT THERE"), 31)
        test.assert_equals(presses("#codewars *rocks"), 36)
