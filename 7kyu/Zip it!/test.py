import codewars_test as test
from kata import lstzip

@test.describe('Initial Tests')
def fixed_tests():
    @test.it("")
    def one():
        a = [1, 2, 3, 4, 5]
        b = ['a','b','c','d','e']
        test.assert_equals(lstzip(a, b, lambda a, b: str(a) + str(b)), ["1a", "2b", "3c", "4d", "5e"]);
        test.assert_equals(lstzip(b, a, lambda a, b: str(a) + str(b)), ["a1", "b2", "c3", "d4", "e5"]);
        test.assert_equals(lstzip(b, lstzip(a, b, lambda a, b: a * ord(b[0])), lambda a, b: str(a) + str(b)),["a97", "b196", "c297", "d400", "e505"])
