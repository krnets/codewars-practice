import codewars_test as test
from kata import are_equally_strong


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(are_equally_strong(10, 15, 15, 10), True)
        test.assert_equals(are_equally_strong(15, 10, 15, 10), True)
        test.assert_equals(are_equally_strong(10, 10, 10, 10), True)
        test.assert_equals(are_equally_strong(15, 10, 15, 9), False)
        test.assert_equals(are_equally_strong(10, 5, 5, 10), True)
        test.assert_equals(are_equally_strong(1, 10, 10, 0), False)
        test.assert_equals(are_equally_strong(10, 5, 11, 4), False)
