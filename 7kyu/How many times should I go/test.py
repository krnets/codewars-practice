import codewars_test as test
from kata import how_many_times


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(how_many_times(40, 15), 3)
        test.assert_equals(how_many_times(30, 10), 3)
        test.assert_equals(how_many_times(80, 15), 6)
