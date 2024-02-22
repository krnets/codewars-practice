import codewars_test as test
from kata import Walker

test.describe("Simple Paths")

w = Walker()
path = "eeee"
w.walk(path)
test.assert_equals(w.coords(), (4, 0))

w = Walker()
path = "wwww"
w.walk(path)
test.assert_equals(w.coords(), (-4, 0))

w = Walker()
path = "nnnn"
w.walk(path)
test.assert_equals(w.coords(), (0, 4))

w = Walker()
path = "ssss"
w.walk(path)
test.assert_equals(w.coords(), (0, -4))
