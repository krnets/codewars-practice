import re
import codewars_test as test


# def reverse_words(text):
#     return "".join(w[::-1] for w in re.findall("[a-z!.]+|\s+", text, re.I))


def reverse_words(text):
    return re.sub(r"\S+", lambda w: w.group()[::-1], text)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            reverse_words("The quick brown fox jumps over the lazy dog."),
            "ehT kciuq nworb xof spmuj revo eht yzal .god",
        )
        test.assert_equals(reverse_words("apple"), "elppa")
        test.assert_equals(reverse_words("a b c d"), "a b c d")
        test.assert_equals(
            reverse_words("double  spaced  words"), "elbuod  decaps  sdrow"
        )
