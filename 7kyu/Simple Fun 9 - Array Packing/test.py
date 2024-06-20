import codewars_test as test
from kata import array_packing

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(array_packing([24, 85, 0]) , 21784)
        test.assert_equals(array_packing([23, 45, 39]) , 2567447)
        test.assert_equals(array_packing([1, 1]) , 257)
        test.assert_equals(array_packing([0]) , 0)
        test.assert_equals(array_packing([255, 255, 255, 255]) , 4294967295)