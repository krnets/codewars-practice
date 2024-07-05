import codewars_test as test
from gmpy2 import fib


# def perimeter(n):
#     a, b = 1, 1
#     for _ in range(n + 2):
#         a, b = b, a + b
#     return 4 * (a - 1)


def perimeter(n):
    return 4 * (fib(n + 3) - 1)


@test.describe("Testing...")
def _():
    @test.it("Fixed tests")
    def _():
        test.assert_equals(perimeter(5), 80)
        test.assert_equals(perimeter(7), 216)
        test.assert_equals(perimeter(20), 114624)
        test.assert_equals(perimeter(30), 14098308)
        test.assert_equals(perimeter(100), 6002082144827584333104)
        test.assert_equals(
            perimeter(500),
            2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504,
        )
