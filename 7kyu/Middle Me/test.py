import codewars_test as test
from kata import middle_me

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(middle_me(18, 'z', '#'), '#########z#########')
        test.assert_equals(middle_me(19, 'z', '#'), 'z')