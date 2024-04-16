import codewars_test as test
from kata import queue

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(queue([2, 5, 3, 6, 4], 0), 6)
        test.assert_equals(queue([2, 5, 3, 6, 4], 1), 18)
        test.assert_equals(queue([2, 5, 3, 6, 4], 2), 12)
        test.assert_equals(queue([2, 5, 3, 6, 4], 3), 20)
        test.assert_equals(queue([2, 5, 3, 6, 4], 4), 17)