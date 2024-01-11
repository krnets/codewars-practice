import codewars_test as test
from kata import arithmetic_sequence_elements

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(arithmetic_sequence_elements(1, 2, 5), '1, 3, 5, 7, 9')
        test.assert_equals(arithmetic_sequence_elements(1, 0, 5), '1, 1, 1, 1, 1')
        test.assert_equals(arithmetic_sequence_elements(1, -3, 10), '1, -2, -5, -8, -11, -14, -17, -20, -23, -26')
        test.assert_equals(arithmetic_sequence_elements(1, 2, 5), '1, 3, 5, 7, 9')
        test.assert_equals(arithmetic_sequence_elements(36, 10, 6), '36, 46, 56, 66, 76, 86')