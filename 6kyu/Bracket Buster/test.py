import codewars_test as test
from kata import bracket_buster

test.assert_equals(bracket_buster("Don't [pass to Ramone]"), ["pass to Ramone"])
test.assert_equals(bracket_buster(1337), "Take a seat on the bench.")
test.assert_equals(bracket_buster("[I'm] glad y'all [set it]] off"), ["I'm", "set it"])
