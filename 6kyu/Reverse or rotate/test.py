from kata import rev_rot
import codewars_test as test


def testing(actual, expected):
    test.assert_equals(actual, expected)


test.describe("revrot")
test.it("Basic tests")
testing(rev_rot("1234", 0), "")
testing(rev_rot("", 0), "")
testing(rev_rot("1234", 5), "")
testing(rev_rot("", 8), "")
testing(rev_rot("123456779", 0), "")
testing(rev_rot("733049910872815764", 5), "330479108928157")
testing(rev_rot("123456987654", 6), "234561876549")
testing(rev_rot("123456987653", 6), "234561356789")
testing(rev_rot("66443875", 4), "44668753")
testing(rev_rot("66443875", 8), "64438756")
testing(rev_rot("664438769", 8), "67834466")
testing(rev_rot("123456779", 8), "23456771")
testing(rev_rot("563000655734469485", 4), "0365065073456944")
