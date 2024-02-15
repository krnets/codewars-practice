import codewars_test as test
from kata import keyword_cipher

abc = "abcdefghijklmnopqrstuvwxyz"
key = "keyword"
cipher = keyword_cipher(abc, key)

test.assert_equals(cipher.encode("abc"), "key")
test.assert_equals(cipher.encode("xyz"), "vxz")
test.assert_equals(cipher.decode("key"), "abc")
test.assert_equals(cipher.decode("vxz"), "xyz")
