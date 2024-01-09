import codewars_test as test
from kata import array_madness


@test.describe("Array Madness")
def fixed_tests():
    @test.it('Simple Test Cases')
    def simple_test_cases():
        test.assert_equals(array_madness([4, 5, 6], [1, 2, 3]), True)
        test.assert_equals(array_madness([1, 2, 3], [4, 5, 6]), False)

    @test.it("Fixed Test Cases")
    def fixed_test():
        test.assert_equals(array_madness([4, 5, 6], [3, 4, 5]), False)
        test.assert_equals(array_madness([3, 4, 5], [2, 3, 4]), False)
        test.assert_equals(array_madness([2, 3, 4], [1, 2, 3]), False)
        test.assert_equals(array_madness([1, 2, 3], [0, 1, 2]), True)
        test.assert_equals(array_madness([5, 3, 2, 4, 1], [15]), False)
        test.assert_equals(array_madness(
            [2, 5, 3, 4, 1], [3, 3, 3, 3, 3]), False)
        test.assert_equals(array_madness([1, 3, 4, 2, 4], [
                           2, 2, 2, 2, 2, 2, 2, 1]), False)
        test.assert_equals(array_madness([1, 2, 3, 4, 5], [
                           2, 2, 2, 2, 2, 2, 1, 1, 1]), True)
        test.assert_equals(array_madness(
            [2, 4, 6, 8, 10, 12, 14], [1, 3, 5, 7, 9, 11, 13]), False)


@test.describe("Random Tests")
def random_tests():
    import random

    def solution(a, b):
        return sum(x ** 2 for x in a) > sum(x ** 3 for x in b)

    for _ in range(666):
        a = random.sample(range(1, 1200), random.randint(1, 11))
        b = random.sample(range(1, 30), random.randint(1, 11))
        expected = solution(a, b)
        actual = array_madness(a, b)

        @test.it(f"testing for array_madness({a}, {b})")
        def test_case():
            test.assert_equals(actual, expected)
