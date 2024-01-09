import codewars_test as test
from kata import calculate_tip


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(calculate_tip(30, "poor"), 2)
        test.assert_equals(calculate_tip(20, "Excellent"), 4)
        test.assert_equals(calculate_tip(20, "hi"), 'Rating not recognised')
        test.assert_equals(calculate_tip(107.65, "GReat"), 17)
        test.assert_equals(calculate_tip(20, "great!"),
                           'Rating not recognised')
