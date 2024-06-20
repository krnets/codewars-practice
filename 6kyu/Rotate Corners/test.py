import codewars_test as test
from kata import rotate_corners

test.describe("Basic Tests")

test.it("[[1, 2], [3, 4]]")
test.assert_equals(rotate_corners([[1, 2], [3, 4]]), [[1, 2], [3, 4]])
test.it("[[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
test.assert_equals(rotate_corners([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 3], [7, 9]])
test.it("[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'z']]")
test.assert_equals(rotate_corners([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'z']]), [['g', 'a'], ['z', 'c']])
test.it("[['!', ':', 7, '^'], [997, 'T', '<', '+'], [47, 'v', 531, 'Q'], ['{', '[', ']', '}']]")
test.assert_equals(rotate_corners([['!', ':', 7, '^'], [997, 'T', '<', '+'], [47, 'v', 531, 'Q'], ['{', '[', ']', '}']]), [['}', '{'], ['^', '!']])
test.it("[[True, 77, False], ['$', '^', 972]]")
test.assert_equals(rotate_corners([[True, 77, False], ['$', '^', 972]]), [[False, 972], [True, '$']])
