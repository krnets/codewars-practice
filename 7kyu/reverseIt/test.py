import codewars_test as test
from kata import reverse_it

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_it('Hello'), "olleH", 'Not quite')
        test.assert_equals(reverse_it(314159), 951413, 'Not quite')
        test.assert_equals(reverse_it("314159"), "951413", 'Not quite')
        test.assert_equals(reverse_it([]), [], 'Not quite')
        test.assert_equals(reverse_it({}), {}, 'Not quite')
        test.assert_equals(reverse_it(True), True, 'Not quite')
        test.assert_equals(reverse_it([1, 2, 3]), [1, 2, 3], 'Not quite')