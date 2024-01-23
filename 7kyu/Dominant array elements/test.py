import codewars_test as test
from kata import solve


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(solve([16, 17, 14, 3, 14, 5, 2]), [17, 14, 5, 2])
        test.assert_equals(solve([92, 52, 93, 31, 89, 87, 77, 105]), [105])
        test.assert_equals(solve([75, 47, 42, 56, 13, 55]), [75, 56, 55])
        test.assert_equals(solve([67, 54, 27, 85, 66, 88, 31, 24, 49]), [88, 49])
        test.assert_equals(solve([76, 17, 25, 36, 29]), [76, 36, 29])
        test.assert_equals(solve([104, 18, 37, 9, 36, 47, 28]), [104, 47, 28])
