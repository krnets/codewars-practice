import codewars_test as test
from kata import highest_rank


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
        test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10)
        test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]), 12)
        test.assert_equals(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]), 3)
        test.assert_equals(highest_rank([1, 2, 3]), 3)
        test.assert_equals(highest_rank([1, 1, 2, 3]), 1)
        test.assert_equals(highest_rank([1, 1, 2, 2, 3]), 2)