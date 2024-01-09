from kata import name_value as user_solution

import codewars_test as test


@test.describe("Fixed tests")
def fixed_tests():
    @test.it("")
    def f():
        test.assert_equals(user_solution(["codewars", "abc", "xyz"]), [88, 12, 225])

        test.assert_equals(user_solution(["abc", "abc abc"]), [6, 24])

        test.assert_equals(
            user_solution(["abc abc", "abc abc", "abc", "abc"]), [12, 24, 18, 24]
        )
