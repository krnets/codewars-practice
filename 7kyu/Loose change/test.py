import codewars_test as test
from kata import change_count

test.assert_equals(change_count('dime penny dollar'), '$1.11')
test.assert_equals(change_count('dime penny nickel'), '$0.16')
test.assert_equals(change_count('quarter quarter'), '$0.50')
test.assert_equals(change_count('dollar penny dollar'), '$2.01')
test.assert_equals(change_count('dollar dollar dollar dollar dollar dollar dollar dollar dollar dollar penny'), '$10.01')