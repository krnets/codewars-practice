import codewars_test as test
from kata import strange_math

@test.describe("Fixed Tests")
def test_group():
    @test.it("Fixed Tests Cases")
    def test_case():
        test.assert_equals(strange_math(11,2), 4, 'Wrong result for (11,2)')
        test.assert_equals(strange_math(15,5), 11, 'Wrong result for (15,5)')
        test.assert_equals(strange_math(15,15), 7, 'Wrong result for (15,15)')