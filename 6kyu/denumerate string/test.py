import codewars_test as test
from kata import denumerate

test.describe("Basic tests")
test.assert_equals(denumerate([(4,'y'),(1,'o'),(3,'t'),(0,'m'),(2,'n')]),'monty')
test.assert_equals(denumerate([(1, '3'), (2, 'l'), (4, 'o'), (3, 'l'), (0, 'h')]),'h3llo')
test.assert_equals(denumerate([(0,'%')]),False)
test.assert_equals(denumerate([(1,'a'),(2,'b')]),False)
test.assert_equals(denumerate(1),False)