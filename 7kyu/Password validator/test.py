import codewars_test as test
from kata import password

test.describe("Basic tests")
test.assert_equals(password("Abcd1234"), True)
test.assert_equals(password("Abcd123"), False)
test.assert_equals(password("abcd1234"), False)
test.assert_equals(password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890"), True)
test.assert_equals(password("ABCD1234"), False)
test.assert_equals(password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,"), True)
test.assert_equals(password("!@#$%^&*()-_+={}[]|\:;?/>.<,"), False)
test.assert_equals(password(""), False)
test.assert_equals(password(" aA1----"), True)
test.assert_equals(password("4aA1----"), True)
