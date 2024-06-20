import codewars_test as test
from kata import pattern


@test.describe("Basic tests")
def basic():
    @test.it("")
    def f():
        test.assert_equals(pattern(1), "1")
        test.assert_equals(pattern(2), "2\n21")
        test.assert_equals(pattern(5), "5\n54\n543\n5432\n54321")
        test.assert_equals(pattern(0), "")
        test.assert_equals(pattern(-25), "")
