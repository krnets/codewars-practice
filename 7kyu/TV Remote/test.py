import codewars_test as test
from kata import tv_remote


@test.describe("Sample tests")
def sample():
    @test.it("Example")
    def example():
        test.assert_equals(tv_remote("codewars"), 36)

    @test.it("Misc")
    def example():
        test.assert_equals(tv_remote("does"), 16)
        test.assert_equals(tv_remote("your"), 23)
        test.assert_equals(tv_remote("solution"), 33)
        test.assert_equals(tv_remote("work"), 20)
        test.assert_equals(tv_remote("for"), 12)
        test.assert_equals(tv_remote("these"), 27)
        test.assert_equals(tv_remote("words"), 25)
