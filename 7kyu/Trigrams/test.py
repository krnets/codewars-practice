import codewars_test as test
from kata import trigrams

@test.describe("Trigrams")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(trigrams("the quick red"), "the he_ e_q _qu qui uic ick ck_ k_r _re red")
        test.assert_equals(trigrams('Hi'),'')