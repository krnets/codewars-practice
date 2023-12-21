import codewars_test as test
from kata import check_exam


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6)
        test.assert_equals(check_exam(["a", "a", "c", "b"], ["a", "a", "b", ""]), 7)
        test.assert_equals(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16)
        test.assert_equals(check_exam(["b", "c", "b", "a"], ["", "a", "a", "c"]), 0)
