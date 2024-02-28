import codewars_test as test
from kata import has_permission

test.assert_equals(has_permission({'books_allow', 'movies_deny'}, 'movies'), False)
test.assert_equals(has_permission({'books_allow', 'movies_deny'}, 'books'), True)
test.assert_equals(has_permission({'*_allow', 'books_allow', 'movies_deny'}, 'games'), True)
test.assert_equals(has_permission({'*_allow', '*_deny'}, 'movies'), False)
test.assert_equals(has_permission({'*_allow', 'movies_deny'}, 'movies'), False)
test.assert_equals(has_permission({'*_deny', 'books_allow', 'movies_deny'}, 'books'), True)
