import codewars_test as test
from kata import binary_pyramid

@test.describe("Sample Tests")
def basic_tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(binary_pyramid(1,4), "1111010")
        test.assert_equals(binary_pyramid(1,6), "101001101")
        test.assert_equals(binary_pyramid(6,20), "1110010110100011")
        test.assert_equals(binary_pyramid(21,60), "1100000100010001010100")