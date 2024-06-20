from typing import Counter
import codewars_test as test


# def duplicate_count(text):
#     freq = Counter(text.lower())
#     return len([(k, v) for k, v in freq.items() if v > 1])


def duplicate_count(text):
    return sum(v > 1 for v in Counter(text.lower()).values())


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(duplicate_count(""), 0)
        test.assert_equals(duplicate_count("abcde"), 0)
        test.assert_equals(duplicate_count("abcdeaa"), 1)
        test.assert_equals(duplicate_count("abcdeaB"), 2)
        test.assert_equals(duplicate_count("Indivisibilities"), 2)
