import codewars_test as test
from kata import connotation


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("True")
    def basic_test_cases():
        test.assert_equals(connotation("A big brown fox caught a bad bunny"), True)

    @test.it("False")
    def basic_test_cases():
        test.assert_equals(connotation("Xylophones can obtain Xenon."), False)

    @test.it("All caps")
    def basic_test_cases():
        test.assert_equals(connotation("CHOCOLATE MAKES A GREAT SNACK"), True)

    @test.it("Random case")
    def basic_test_cases():
        test.assert_equals(connotation("All FOoD tAsTEs NIcE for someONe"), True)

    @test.it("Random number of spaces")
    def basic_test_cases():
        test.assert_equals(connotation("Is  this the  best  Kata?"), True)

    @test.it("Random test 1")
    def basic_test_cases():
        test.assert_equals(connotation("s smpj geiruzl jbkwkb x owz"), True)

    @test.it("Random test 2")
    def basic_test_cases():
        test.assert_equals(connotation("ajsqpts hsrxelx m"), True)

    @test.it("Random test 3")
    def basic_test_cases():
        test.assert_equals(
            connotation("tbddxq abupox ip pilx kpvshol gxt szqn fbqsxdb dzpmsh kskoc"),
            True,
        )
