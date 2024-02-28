import codewars_test as test
from kata import mispelled


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(mispelled("versed", "xersed"), True)
        test.assert_equals(mispelled("versed", "applb"), False)
        test.assert_equals(mispelled("versed", "v5rsed"), True)
        test.assert_equals(mispelled("1versed", "versed"), True)
        test.assert_equals(mispelled("versed", "versed"), True)
