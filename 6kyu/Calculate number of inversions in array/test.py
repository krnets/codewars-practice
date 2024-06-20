import codewars_test as test
from kata import count_inversions

@test.describe("Sample tests")
def sample_tests():
    @test.it("Tests")
    def _():
        test.assert_equals(count_inversions([]), 0)
        test.assert_equals(count_inversions([1,2,3]), 0)
        test.assert_equals(count_inversions([2,1,3]), 1)
        test.assert_equals(count_inversions([6,5,4,3,2,1]), 15)
        test.assert_equals(count_inversions([6,5,4,3,3,3,3,2,1]), 30)