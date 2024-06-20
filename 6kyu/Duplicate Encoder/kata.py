from collections import Counter
import codewars_test as test


def duplicate_encode(word):
    word = word.lower()
    freq = Counter(word)
    return "".join("(" if freq[c] == 1 else ")" for c in word)


@test.describe("Duplicate Encoder")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(duplicate_encode("din"), "(((")
        test.assert_equals(duplicate_encode("recede"), "()()()")
        test.assert_equals(duplicate_encode("Success"), ")())())", "should ignore case")
        test.assert_equals(duplicate_encode("(( @"), "))((")
