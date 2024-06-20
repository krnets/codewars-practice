import codewars_test as test


def high(x):
    scores = [(score(word), word) for word in x.split()]
    highest = max(scores)[0]
    return next(word for score, word in scores if score == highest)


def score(word):
    offset = ord("a") - 1
    return sum(ord(c) - offset for c in word)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(high("man i need a taxi up to ubud"), "taxi")
        test.assert_equals(high("what time are we climbing up the volcano"), "volcano")
        test.assert_equals(high("take me to semynak"), "semynak")
        test.assert_equals(high("aa b"), "aa")
        test.assert_equals(high("b aa"), "b")
        test.assert_equals(high("bb d"), "bb")
        test.assert_equals(high("d bb"), "d")
        test.assert_equals(high("aaa b"), "aaa")
