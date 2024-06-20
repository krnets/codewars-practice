import codewars_test as test
from kata import transpose

@test.describe('Test case')
def _():
    @test.it('Basic Test')
    def _():
        test.assert_equals(transpose([[1]]), [[1]])
        test.assert_equals(transpose([[1, 2, 3]]), [[1], [2], [3]])
        test.assert_equals(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                           [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        test.assert_equals(transpose([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]),
                           [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]])