import codewars_test as test
from kata import mean_vs_median

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(mean_vs_median([1, 1, 1]), "same")
        test.assert_equals(mean_vs_median([1, 2, 37]), "mean")
        test.assert_equals(mean_vs_median([7, 14, -70]), "median")
        test.assert_equals(mean_vs_median([-10, 20, 5]), 'same')