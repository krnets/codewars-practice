import codewars_test as test
from kata import geometric_sequence_elements

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(geometric_sequence_elements(2, 3, 5), '2, 6, 18, 54, 162')
        test.assert_equals(geometric_sequence_elements(2, 2, 10), '2, 4, 8, 16, 32, 64, 128, 256, 512, 1024')
        test.assert_equals(geometric_sequence_elements(1, -2, 10), '1, -2, 4, -8, 16, -32, 64, -128, 256, -512')