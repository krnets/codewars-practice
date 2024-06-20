import codewars_test as test
from kata import distribution_of


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(distribution_of([4, 7, 2, 9, 5, 2]), [11, 18])
        test.assert_equals(distribution_of([10, 1000, 2, 1]), [12, 1001])
