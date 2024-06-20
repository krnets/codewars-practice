import re
import string
from random import randint, choice, shuffle
from string import ascii_lowercase as abc
import codewars_test as test

REGEX = rf"\A *{'* *'.join(list(abc))}* *\Z"

sensei_regex = re.compile(
    r"^ *a* *b* *c* *d* *e* *f* *g* *h* *i* *j* *k* *l* *m* *n* *o* *p* *q* *r* *s* *t* *u* *v* *w* *x* *y* *z* *\Z"
)
warior_regex = re.compile(REGEX)
SHOULD_NOT_MATCH_FAIL_MSG = ""
SHOULD_MATCH_FAIL_MSG = ""
DIFFERENT_MATCHES_FAIL_MSG = ""
VALID, NOT_VALID = "", ""


def validate_regex_on_list(word_list):
    for word in word_list:
        sensei_match = sensei_regex.match(word)
        warior_match = warior_regex.match(word)
        if (sensei_match == None) != (warior_match == None):
            if warior_match != None:
                test.fail(SHOULD_NOT_MATCH_FAIL_MSG.format(word))
            if warior_match == None:
                test.fail(SHOULD_MATCH_FAIL_MSG.format(word))
        elif sensei_match != None:
            test.assert_equals(
                sensei_match.group(),
                warior_match.group(),
                DIFFERENT_MATCHES_FAIL_MSG.format(word),
            )
        else:
            test.pass_()


VOCABULARY = string.ascii_lowercase + "     "


@test.describe("Fixed Tests")
def fixed_tests():

    @test.it("Valid")
    def valid():
        validate_regex_on_list(VALID)

    @test.it("Not valid")
    def not_valid():
        validate_regex_on_list(NOT_VALID)


@test.describe("Valid")
def random_valid():

    def one_letter_word_with_spaces(c):
        lst = [
            x
            for x in (
                c * randint(0, 6) + " " * randint(0, 3) if randint(0, 10) > 8 else ""
            )
        ]
        shuffle(lst)
        return "".join(lst)

    def generate_valid():
        return "".join([one_letter_word_with_spaces(c) for c in VOCABULARY])

    @test.it("valid")
    def valid():
        AMMOUNT = 200
        validate_regex_on_list([generate_valid() for _ in range(AMMOUNT)])

    @test.it("Empty words")
    def empty():
        validate_regex_on_list(["", " "])

    @test.it("Tabs and newlines are not spaces")
    def tabs_and_newlines():
        validate_regex_on_list(["\t", "\n", "a\t", "a\n", "a\tb", "ab\ncd", "abcdef\n"])


@test.describe("Random Words")
def random_words():

    def fully_random_word(vocabulary):
        return "".join([choice(vocabulary) for _ in range(randint(1, 6))])

    @test.it("Random with allowed characters")
    def random1():
        AMMOUNT = 400
        words = [fully_random_word(VOCABULARY) for _ in range(AMMOUNT)]
        validate_regex_on_list(words)

    @test.it("Fully Random")
    def random2():
        AMMOUNT = 400
        vocabulary = string.printable
        words = [fully_random_word(vocabulary) for _ in range(AMMOUNT)]
        validate_regex_on_list(words)
