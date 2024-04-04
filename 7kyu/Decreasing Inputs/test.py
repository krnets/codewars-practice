import codewars_test as test
from kata import add

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(add(), 0, 'No arguments should return 0')
        test.assert_equals(add(100, 200, 300), 300)
        test.assert_equals(add(2), 2)
        test.assert_equals(add(4, -3, -2), 2)
        test.assert_equals(add(-1, -2, -3, -4), -4)