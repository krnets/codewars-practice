import codewars_test as test
from kata import solution


@test.describe("Example Tests")
def example_tests():
    @test.it("Example Tests")
    def example_tests():
        test.assert_equals(solution("abcdeb", "b"), 2)
        test.assert_equals(solution("abc", "b"), 1)
        test.assert_equals(solution("abbc", "bb"), 1)
        test.assert_equals(solution("abcdeb", "b"), 2)
        test.assert_equals(solution("abcdeb", "a"), 1)
        test.assert_equals(solution("ccddeeccddeecc", "cc"), 3)
        test.assert_equals(solution("aabb", "cc"), 0)
        test.assert_equals(solution("bbaa", "a"), 2)
        test.assert_equals(solution("abab", "a"), 2)
        test.assert_equals(solution("abcdefdvbhibjkb", "b"), 4)
        test.assert_equals(solution("abccded", "cc"), 1)
        test.assert_equals(solution("abccded", "d"), 2)
