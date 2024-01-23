import codewars_test as test
from kata import count_consonants


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(count_consonants("sillystring"), 7)
        test.assert_equals(count_consonants("aeiou"), 0)
        test.assert_equals(count_consonants("abcdefghijklmnopqrstuvwxyz"), 21)
        test.assert_equals(count_consonants("Count my unique consonants!!"), 7)
