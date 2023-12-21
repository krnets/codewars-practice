import codewars_test as test
from kata import house_of_cats


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(house_of_cats(6), [1, 3])
        test.assert_equals(house_of_cats(2), [1])
        test.assert_equals(house_of_cats(4), [0, 2])
        test.assert_equals(house_of_cats(8), [0, 2, 4])
        test.assert_equals(house_of_cats(10), [1, 3, 5])
        test.assert_equals(house_of_cats(36), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
        test.assert_equals(house_of_cats(39), [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
        test.assert_equals(house_of_cats(44), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])
        test.assert_equals(house_of_cats(48), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
        test.assert_equals(house_of_cats(60), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
        test.assert_equals(house_of_cats(94), [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47 ])
        test.assert_equals(house_of_cats(98), [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])
