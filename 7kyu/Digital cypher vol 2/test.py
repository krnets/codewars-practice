import codewars_test as test
from kata import decode


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(decode([20, 12, 18, 30, 21], 1939), "scout")
        test.assert_equals(
            decode([14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8], 1939), "masterpiece"
        )
