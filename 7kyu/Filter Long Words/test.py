import codewars_test as test
from kata import filter_long_words

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(
            filter_long_words('The quick brown fox jumps over the lazy dog', 4),
            ['quick', 'brown', 'jumps'])
        test2 = 'Write a function filter_long_words() that takes a sentence and an ' \
               'integer n and returns the list of words that are longer than n.'
        test.assert_equals(filter_long_words(test2, 4), ['Write', 'function', 'filter_long_words()', 'takes', 'sentence', 'integer', 'returns', 'words', 'longer'])
        test.assert_equals(filter_long_words(test2, 5), ['function', 'filter_long_words()', 'sentence', 'integer', 'returns', 'longer'])
        test.assert_equals(filter_long_words(test2, 6), ['function', 'filter_long_words()', 'sentence', 'integer', 'returns'])
        test.assert_equals(filter_long_words(test2, 7), ['function', 'filter_long_words()', 'sentence'])
        test.assert_equals(filter_long_words(test2, 8), ['filter_long_words()'])