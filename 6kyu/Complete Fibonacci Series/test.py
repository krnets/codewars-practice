import codewars_test as test
from kata import fibonacci

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(fibonacci(4), [0, 1, 1, 2], 'Should work for 4.')
        test.assert_equals(fibonacci(1), [0], 'Should work for 1 element.')
        test.assert_equals(fibonacci(0), [], 'Should have 0 elements for 0.')
        test.assert_equals(fibonacci(-1), [], 'Should have 0 elements for negative input.')
        test.assert_equals(fibonacci(-14), [], 'Should have 0 elements for negative input.')
        test.assert_equals(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 'Should work for 10.')