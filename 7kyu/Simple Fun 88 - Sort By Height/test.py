import codewars_test as test
from kata import sort_by_height

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sort_by_height([-1, 150, 190, 170, -1, -1, 160, 180]),[-1, 150, 160, 170, -1, -1, 180, 190])
        test.assert_equals(sort_by_height([-1, -1, -1, -1, -1]),[-1, -1, -1, -1, -1])
        test.assert_equals(sort_by_height([4, 2, 9, 11, 2, 16]),[2, 2, 4, 9, 11, 16])