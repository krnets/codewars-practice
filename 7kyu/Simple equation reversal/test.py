import codewars_test as test
from kata import solve

test.it("Basic tests")
test.assert_equals(solve("100*b/y"), "y/b*100")
test.assert_equals(solve("a+b-c/d*30"), "30*d/c-b+a")
test.assert_equals(solve("a*b/c+50"), "50+c/b*a")
