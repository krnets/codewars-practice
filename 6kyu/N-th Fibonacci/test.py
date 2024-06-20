import codewars_test as test
import random
from kata import nth_fib


@test.describe("N-th Fibonacci")
def tests():
    def testing(actual, expected):
        test.assert_equals(actual, expected)

    @test.it("Fixed tests")
    def sample_tests():
        test.assert_equals(nth_fib(1), 0, "nth_fib(1) = 0")
        test.assert_equals(nth_fib(2), 1, "nth_fib(2) = 1")
        test.assert_equals(nth_fib(3), 1, "nth_fib(3) = 1")
        test.assert_equals(nth_fib(4), 2, "nth_fib(4) = 2")
        test.assert_equals(nth_fib(5), 3, "nth_fib(5) = 3")
        test.assert_equals(nth_fib(6), 5, "nth_fib(6) = 5")
        test.assert_equals(nth_fib(7), 8, "nth_fib(7) = 8")

    @test.it("Random tests")
    def random_tests():
        def ref_solution(n):
            if n < 2:
                return n - 1
            a, b = 0, 1
            for _ in range(2, n):
                a, b = b, a + b
            return b

        for _ in range(10):
            N = random.randint(1, 40)
            expected = ref_solution(N)
            actual = nth_fib(N)
            test.assert_equals(actual, expected, f"nth_fib({N}) = {expected}")
