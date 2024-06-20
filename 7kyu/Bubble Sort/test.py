import codewars_test as test
from kata import bubble

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        l=[1,2,4,3]
        sol=[[1,2,3,4]]
        test.assert_equals(bubble(l), sol)

        l=[2,1,4,3]
        sol=[[1,2,4,3],[1,2,3,4]]
        test.assert_equals(bubble(l), sol)

        l=[1,4,3,6,7,9,2,5,8]
        sol=[[1, 3, 4, 6, 7, 9, 2, 5, 8],
            [1, 3, 4, 6, 7, 2, 9, 5, 8],
            [1, 3, 4, 6, 7, 2, 5, 9, 8],
            [1, 3, 4, 6, 7, 2, 5, 8, 9],
            [1, 3, 4, 6, 2, 7, 5, 8, 9],
            [1, 3, 4, 6, 2, 5, 7, 8, 9],
            [1, 3, 4, 2, 6, 5, 7, 8, 9],
            [1, 3, 4, 2, 5, 6, 7, 8, 9],
            [1, 3, 2, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]]
        test.assert_equals(bubble(l), sol)

