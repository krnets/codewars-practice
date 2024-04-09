import codewars_test as test
from kata import pattern

@test.describe("Basic tests")
def f():
    @test.it("")
    def f():
        test.assert_equals(pattern(7),"1234567\n2345671\n3456712\n4567123\n5671234\n6712345\n7123456")
        test.assert_equals(pattern(1),"1")
        test.assert_equals(pattern(4),"1234\n2341\n3412\n4123")
        test.assert_equals(pattern(0),"")
        test.assert_equals(pattern(-25),"")