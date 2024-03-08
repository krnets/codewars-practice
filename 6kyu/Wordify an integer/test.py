import codewars_test as test
from kata import wordify

@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        test.assert_equals(wordify(1), "one", "1 should be one.")
        test.assert_equals(wordify(10), "ten", "10 should be ten.")
        test.assert_equals(wordify(12), "twelve", "12 should be twelve.")
        test.assert_equals(wordify(17), "seventeen", "17 should be seventeen.")
        test.assert_equals(wordify(56), "fifty six", "56 should be fifty six.")
        test.assert_equals(wordify(90), "ninety", "90 should be ninety.")
        test.assert_equals(wordify(100), "one hundred", "100 should be one hundred.")
        test.assert_equals(wordify(326), "three hundred twenty six", "326 should be three hundred twenty six.")