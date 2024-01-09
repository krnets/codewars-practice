from re import sub
from random import choice, randint
from string import ascii_letters, punctuation
import codewars_test as test
from kata import remove

test.describe("Basic Tests")

tests = [
    # [input, expected],
    ["Hi!", "Hi"],
    ["Hi!!!", "Hi"],
    ["!Hi", "!Hi"],
    ["!Hi!", "!Hi"],
    ["Hi! Hi!", "Hi! Hi"],
    ["Hi", "Hi"],
]

for inp, exp in tests:
    test.assert_equals(remove(inp), exp)

test.describe("Random Tests")


CHARS = ascii_letters + punctuation


def create_word(length):
    return "".join(choice(CHARS) for _ in range(length))


def add_excl(word):
    return "%s%s%s" % (randint(0, 20) * "!", word, randint(0, 20) * "!")


def create_sentence(length):
    return " ".join(
        create_word(randint(0, 15))
        if randint(0, 30) % 3
        else add_excl(create_word(randint(0, 15)))
        for _ in range(length)
    )


def reference(s):
    return sub("!+$", "", s)


for _ in range(100):
    s = create_sentence(randint(1, 100))
    test.assert_equals(remove(s), reference(s))
