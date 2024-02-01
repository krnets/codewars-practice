from kata import expanded_form
import codewars_test as test


@test.describe("Example tests")
def example_tests():
    @test.it("Examples")
    def examples():
        test.assert_equals(expanded_form(1.24), "1 + 2/10 + 4/100")
        test.assert_equals(expanded_form(7.304), "7 + 3/10 + 4/1000")
        test.assert_equals(expanded_form(0.04), "4/100")
        test.assert_equals(expanded_form(807.304), "800 + 7 + 3/10 + 4/1000")
