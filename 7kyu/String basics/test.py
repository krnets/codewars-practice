import codewars_test as test
from kata import get_users_ids

test.describe("Basic tests")
test.assert_equals(get_users_ids("uid12345"), ["12345"])
test.assert_equals(get_users_ids("   uidabc  "), ["abc"])
test.assert_equals(get_users_ids("#uidswagger"), ["swagger"])
test.assert_equals(get_users_ids("uidone, uidtwo"), ["one", "two"])
test.assert_equals(get_users_ids("uidCAPSLOCK"), ["capslock"])

test.describe("Advanced tests")
test.assert_equals(get_users_ids("uid##doublehashtag"), ["doublehashtag"])
test.assert_equals(get_users_ids("  uidin name whitespace"), ["in name whitespace"])
test.assert_equals(get_users_ids("uidMultipleuid"), ["multipleuid"])
test.assert_equals(get_users_ids("uid12 ab, uid#, uidMiXeDcHaRs"), ["12 ab", "", "mixedchars"])
test.assert_equals(get_users_ids(" uidT#e#S#t# "), ["test"])