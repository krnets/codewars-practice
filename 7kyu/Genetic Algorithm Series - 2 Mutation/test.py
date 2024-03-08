import codewars_test as test
from kata import mutate


@test.describe("mutate")
def __():
    zero = "0" * 100
    one = "1" * 100

    @test.it("100% mutate")
    def _():
        test.assert_equals(mutate(zero, 1), one)
        test.assert_equals(mutate(one, 1), zero)

    @test.it("0% mutate")
    def _():
        test.assert_equals(mutate(zero, 0), zero)
        test.assert_equals(mutate(one, 0), one)

    @test.it("50% mutate")
    def _():
        test.expect("0" in mutate(zero, 0.5))
        test.expect("1" in mutate(one, 0.5))
