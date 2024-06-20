import codewars_test as test
from kata import solve

test.it("Basic tests")
test.assert_equals(solve("code*s","codewars"),True)
test.assert_equals(solve("codewar*s","codewars"), True)
test.assert_equals(solve("code*warrior","codewars"),False)
test.assert_equals(solve("c","c"),True)
test.assert_equals(solve("*s","codewars"),True)
test.assert_equals(solve("*s","s"), True)
test.assert_equals(solve("s*","s"),True)
test.assert_equals(solve("aa","aaa"), False)
test.assert_equals(solve("aa*","aaa"), True)
test.assert_equals(solve("aaa","aa"), False)
test.assert_equals(solve("aaa*","aa"), False)
test.assert_equals(solve("*","codewars"),True)