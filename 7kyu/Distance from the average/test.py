import codewars_test as test
from kata import distances_from_average

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(distances_from_average([55, 95, 62, 36, 48]), [4.2, -35.8, -2.8, 23.2, 11.2])
        test.assert_equals(distances_from_average([1, 1, 1, 1, 1]), [0, 0, 0, 0, 0])
        test.assert_equals(distances_from_average([1, -1, 1, -1, 1, -1]), [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0])
        test.assert_equals(distances_from_average([1, -1, 1, -1, 1]), [-0.8, 1.2, -0.8, 1.2, -0.8])
        test.assert_equals(distances_from_average([2, -2]), [-2.0, 2.0])
        test.assert_equals(distances_from_average([1]), [0])
        test.assert_equals(distances_from_average([123, -65, 32432, -353, -534]), [6197.6, 6385.6, -26111.4, 6673.6, 6854.6])
        test.assert_equals(distances_from_average(range(101)), list(range(50,-51,-1)))
        test.assert_equals(distances_from_average(range(1001)), list(range(500,-501,-1)))
        test.assert_equals(distances_from_average(range(1000001)), list(range(500000,-500001,-1)))