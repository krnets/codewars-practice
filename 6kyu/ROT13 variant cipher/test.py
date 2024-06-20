import codewars_test as test
from kata import encrypter


test.describe("Basic tests")
test.assert_equals(encrypter("amz"), "man",)
test.assert_equals(encrypter("welcome to the organization"), "qibkyai ty tfi yvgmzenmteyz", "Expect 'welcome to our organization' to return 'qibkyai ty ysv yvgmzenmteyz'")
test.assert_equals(encrypter("hello"), "fibby", "Expect 'hello' to return 'fibby'")
test.assert_equals(encrypter("my name is"), "ao zmai eu", "Expect 'my name is' to return 'ao zmai eu'")
test.assert_equals(encrypter("goodbye"), "gyyjloi", "Expect 'goodbye' to return 'gyyjloi'")