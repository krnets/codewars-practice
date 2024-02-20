import codewars_test as test
from kata import length_of_sequence

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(length_of_sequence([1], 0), 0, 'Returns zero when the element is not found in the array')
        test.assert_equals(length_of_sequence([1], 1), 0, 'Returns zero with only one element in the array')
        test.assert_equals(length_of_sequence([1, 1], 1), 2, 'Returns two when there are only two elements in the array');
        test.assert_equals(length_of_sequence([1, 2, 3, 1], 1), 4, 'Returns four for an array of length four and the number to be searched at the boundaries');
        test.assert_equals(length_of_sequence([-7, 5, 0, 2, 9, 5], 5), 5, 'Returns five');
        test.assert_equals(length_of_sequence([-7, 6, 2, -7, 4], -7), 4, 'Returns four');
        test.assert_equals(length_of_sequence([0, 8, -7, 6, 1, 2, -7, 4, 8, 9], 8), 8, 'Returns eight')
        test.assert_equals(length_of_sequence([-7, 3, -7, -7, 2, 1], -7), 0, 'Returns zero as when there are more than two instances')
        test.assert_equals(length_of_sequence([-7, 3, -7, -7, 2, -7], -7), 0, 'Returns zero as when there are more than two instances')