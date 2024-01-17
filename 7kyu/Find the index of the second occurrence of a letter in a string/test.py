import codewars_test as test
from kata import second_symbol


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(second_symbol('Hello world!!!','l'), 3, 'Find the index of the second symbol "l" in the string')
        test.assert_equals(second_symbol('Hello world!!!', 'o'), 7, 'Find the index of the second symbol "o" in the string')
        test.assert_equals(second_symbol('Hello world!!!', 'A'), -1, 'The symbol "A" is not in the string')
        test.assert_equals(second_symbol('', 'q'), -1, 'The symbol "q" is not in the string')
        test.assert_equals(second_symbol('Hello', '!'), -1, 'The symbol "!" is not in the string')
        test.assert_equals(second_symbol('DYpoIwlbckWZ', 'p'), -1)