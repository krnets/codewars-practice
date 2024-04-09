import codewars_test as test
from kata import sc

@test.describe("Sample tests")
def sample_tests():
    @test.it("Tests")
    def it_1():
        test.assert_equals(sc("+"), 1)
        test.assert_equals(sc("-"), 1)
        test.assert_equals(sc("+-"), 8)
        test.assert_equals(sc("-+"), 8)
        test.assert_equals(sc("---+++"), 16)
        test.assert_equals(sc("-+-+-+"), 36)
        test.assert_equals(sc("-+-+-----------"), 49)
        test.assert_equals(sc("-+-+-++++++++++"), 54)