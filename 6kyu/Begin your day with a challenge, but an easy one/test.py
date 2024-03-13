import codewars_test as test
from kata import one_two_three


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(one_two_three(0), [0, 0])
        test.assert_equals(one_two_three(1), [1, 1])
        test.assert_equals(one_two_three(2), [2, 11])
        test.assert_equals(one_two_three(3), [3, 111])
        test.assert_equals(one_two_three(19), [991, 1111111111111111111])
        test.assert_equals(one_two_three(21), [993, 111111111111111111111])
        test.assert_equals(one_two_three(25), [997, 1111111111111111111111111])

        test.assert_equals(
            one_two_three(234),
            [
                99999999999999999999999999,
                111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
            ],
        )
