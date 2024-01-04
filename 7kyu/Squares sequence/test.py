import codewars_test as test
from kata import squares


@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(squares(2, 5), [2, 4, 16, 256, 65536])
        test.assert_equals(squares(3, 3), [3, 9, 81])
        test.assert_equals(squares(5, 3), [5, 25, 625])
        test.assert_equals(squares(10, 4), [10, 100, 10000, 100000000])
        test.assert_equals(squares(2, 0), [])
        test.assert_equals(squares(2, -4), [])