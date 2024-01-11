import codewars_test as test
from kata import missing_no


@test.describe("Example Tests")
def exampleTests():
    @test.it("Basic tests")
    def examples():
        # Numbers from 0 to 100, but missing 5
        nums = list(range(0, 101))
        nums.remove(5)
        test.assert_equals(missing_no(nums), 5)

        nums = list(reversed(range(0, 101)))
        nums.remove(10)
        test.assert_equals(missing_no(nums), 10)
