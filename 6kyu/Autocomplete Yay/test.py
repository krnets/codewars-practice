import codewars_test as test
from kata import autocomplete


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        dictionary = [
            "abnormal",
            "arm-wrestling",
            "absolute",
            "airplane",
            "airport",
            "amazing",
            "apple",
            "ball",
        ]

        test.assert_equals(autocomplete("ai", dictionary), ["airplane", "airport"])
        test.assert_equals(
            autocomplete("a", dictionary),
            ["abnormal", "arm-wrestling", "absolute", "airplane", "airport"],
        )
