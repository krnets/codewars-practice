import codewars_test as test
from kata import perfect_roots


@test.describe("Example Tests")
def example_tests():
    @test.it("Example Test Case")
    def example_test_case():
        test.assert_equals(perfect_roots(256), True)
        test.assert_equals(perfect_roots(1000), False)
        test.assert_equals(perfect_roots(6561), True)
