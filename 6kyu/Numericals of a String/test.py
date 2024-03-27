import codewars_test as test
from kata import numericals

test.assert_equals(numericals("Hello, World!"), "1112111121311")
test.assert_equals(numericals("Hello, World! It's me, JomoPipi!"), "11121111213112111131224132411122")
test.assert_equals(numericals("hello hello"), "11121122342")
test.assert_equals(numericals("Hello"), "11121")
test.assert_equals(numericals("aaaaaaaaaaaa"),"123456789101112")