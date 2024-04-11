import codewars_test as test
from kata import next_higher


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(next_higher(128), 256)
        test.assert_equals(next_higher(1), 2)
        test.assert_equals(next_higher(1022), 1279)
        test.assert_equals(next_higher(127), 191)
        test.assert_equals(next_higher(1253343), 1253359)
