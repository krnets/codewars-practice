import codewars_test as test
from kata import well


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            well([["bad", "bAd", "bad"], ["bad", "bAd", "bad"], ["bad", "bAd", "bad"]]),
            "Fail!",
        )
        test.assert_equals(
            well(
                [
                    ["gOOd", "bad", "BAD", "bad", "bad"],
                    ["bad", "bAd", "bad"],
                    ["GOOD", "bad", "bad", "bAd"],
                ]
            ),
            "Publish!",
        )
        test.assert_equals(
            well(
                [["gOOd", "bAd", "BAD", "bad", "bad", "GOOD"], ["bad"], ["gOOd", "BAD"]]
            ),
            "I smell a series!",
        )
