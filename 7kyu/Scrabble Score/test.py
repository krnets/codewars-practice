import codewars_test as test
from kata import scrabble_score

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(scrabble_score(""), 0, "returns 0 for ''")
        test.assert_equals(scrabble_score('a'), 1, 'returns 1 for a')
        test.assert_equals(scrabble_score("street"), 6, 'returns 6 for street')
        test.assert_equals(scrabble_score("STREET"), 6, 'returns 6 for STREET')
        test.assert_equals(scrabble_score(' a'), 1, 'returns score of " a" (with space)')
        test.assert_equals(scrabble_score("st re et"), 6, 'returns 6 for street with whitespaces')
        test.assert_equals(scrabble_score('f'), 4, 'returns 4 for f')
        test.assert_equals(scrabble_score("quirky"), 22, 'returns 22 for quirky')
        test.assert_equals(scrabble_score("MULTIBILLIONAIRE"), 20, 'returns 20 for MULTIBILLIONAIRE')
        test.assert_equals(scrabble_score("alacrity"), 13, 'returns 13 for alacrity')