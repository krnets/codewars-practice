from kata import new_avg
import codewars_test as test


@test.describe("new_avg")
def _():
    @test.it("Basic tests")
    def _():
        test.assert_equals(new_avg([14, 30, 5, 7, 9, 11, 16], 90), 628)
        test.assert_equals(new_avg([14, 30, 5, 7, 9, 11, 15], 92), 645)

        test.expect_error(
            "Error expected", lambda: new_avg([14, 30, 5, 7, 9, 11, 15], 2)
        )
