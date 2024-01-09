import codewars_test as test
from kata import encode


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(encode("scout", 1939), [20, 12, 18, 30, 21])
        test.assert_equals(
            encode("masterpiece", 1939), [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]
        )
