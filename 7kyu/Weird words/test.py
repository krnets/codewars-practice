import codewars_test as test
from kata import next_letter

@test.describe("Sample tests")
def tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(next_letter("Hello"), "Ifmmp")
        test.assert_equals(next_letter("What is your name?"), "Xibu jt zpvs obnf?")
        test.assert_equals(next_letter("zOo"), "aPp")