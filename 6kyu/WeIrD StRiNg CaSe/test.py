import codewars_test as test
from kata import to_weird_case


@test.describe("to_weird_case")
def to_weird_case():
    @test.it("should return the correct value for a single word")
    def single_words_tests():
        test.assert_equals(to_weird_case("This"), "ThIs")
        test.assert_equals(to_weird_case("is"), "Is")

    @test.it("should return the correct value for multiple words")
    def multiple_words_tests():
        test.assert_equals(to_weird_case("THIs iS a TEST"), "ThIs Is A TeSt")
