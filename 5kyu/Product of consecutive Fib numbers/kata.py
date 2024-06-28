import codewars_test as test


def product_fib(_prod):
    a, b = 0, 1
    while a * b < _prod:
        a, b = b, a + b
    return [a, b, a * b == _prod]


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(product_fib(4895), [55, 89, True])
        test.assert_equals(product_fib(5895), [89, 144, False])
