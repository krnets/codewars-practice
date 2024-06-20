import codewars_test as test
from kata import count_correct_characters

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(count_correct_characters("dog", "car"), 0, "Expected 0")
        test.assert_equals(count_correct_characters("dog", "god"), 1, "Expected 1")
        test.assert_equals(count_correct_characters("dog", "cog"), 2, "Expected 2")
        test.assert_equals(count_correct_characters("dog", "cod"), 1, "Expected 1")
        test.assert_equals(count_correct_characters("dog", "bog"), 2, "Expected 2")
        test.assert_equals(count_correct_characters("dog", "dog"), 3, "Expected 3")