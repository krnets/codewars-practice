import codewars_test as test
from kata import valid_number

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(valid_number("0.00"),True)
        test.assert_equals(valid_number(".00"),True)
        test.assert_equals(valid_number("-.00"),True)
        test.assert_equals(valid_number(".30"),True)
        test.assert_equals(valid_number("0.40"),True)
        test.assert_equals(valid_number("34443.33"),True)
        test.assert_equals(valid_number(".0a"),False)
        test.assert_equals(valid_number("1.00."),False)
        test.assert_equals(valid_number(".+00"),False)
        test.assert_equals(valid_number("w.00"),False)
        test.assert_equals(valid_number("..00"),False)
        test.assert_equals(valid_number("1,00"),False)
