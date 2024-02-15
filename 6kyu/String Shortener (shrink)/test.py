import codewars_test as test
from kata import shorten

sentence = "The quick brown fox jumps over the lazy dog"
res = shorten(sentence, 27)

test.assert_equals(len(res), 27, "Length is not 27")
test.assert_equals(res, "The quick br...the lazy dog", "result does not match")

res2 = shorten(sentence, 27, "----")

test.assert_equals(len(res2), 27, "Length is not 27")
test.assert_equals(res2, "The quick b----the lazy dog", "result does not match")
