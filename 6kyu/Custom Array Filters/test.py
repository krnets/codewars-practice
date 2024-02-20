import codewars_test as test
from kata import list

test.assert_equals(list([1,2,3,4,5]).even(), [2,4], "Nope")
test.assert_equals(list([1,2,3,4,5]).odd(), [1,3,5], "Nope")