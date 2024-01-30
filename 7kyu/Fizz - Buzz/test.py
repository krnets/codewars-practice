import codewars_test as test
from kata import solution


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(solution(20), [5, 2, 1])
        test.assert_equals(solution(2), [0, 0, 0])
        test.assert_equals(solution(14), [4, 2, 0])
        test.assert_equals(solution(30), [8, 4, 1])
        test.assert_equals(solution(141), [37, 19, 9])