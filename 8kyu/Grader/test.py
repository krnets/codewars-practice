from kata import grader
import codewars_test as test

test.assert_equals(grader(1), "A")
test.assert_equals(grader(1.01), "F")
test.assert_equals(grader(0.2), "F")
test.assert_equals(grader(0.7), "C")
test.assert_equals(grader(0.8), "B")
test.assert_equals(grader(0.9), "A")
test.assert_equals(grader(0.6), "D")
test.assert_equals(grader(0.5), "F")
test.assert_equals(grader(0), "F")