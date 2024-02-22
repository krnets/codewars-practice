import codewars_test as test
from kata import longest_sequence

@test.describe("Example test cases")
def sample_tests():
    test.assert_equals(longest_sequence([1, 2, 2, 1, 2, 1, 2, 2, 2], 2), 3)
    test.assert_equals(longest_sequence(["a", "a", "b", "c", "a", "d", "a", "a"], "a"), 2)
    test.assert_equals(longest_sequence([0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1], 1), 4)