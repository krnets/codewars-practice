from kata import valid_parentheses
import codewars_test as test


def run_test(expected, input):
    test.assert_equals(
        valid_parentheses(input), expected, f'Test failed for input: "{input}"'
    )


@test.describe("Sample tests")
def sample_tests():
    @test.it("Should return True for valid parentheses")
    def valid_cases():
        run_test(True, "()")
        run_test(True, "((()))")
        run_test(True, "()()()")
        run_test(True, "(()())()")
        run_test(True, "()(())((()))(())()")

    @test.it("Should return False for invalid parentheses")
    def invalid_cases():
        run_test(False, ")(")
        run_test(False, "()()(")
        run_test(False, "((())")
        run_test(False, "())(()")
        run_test(False, ")()")
        run_test(False, ")")

    @test.it("Should return True for empty strings")
    def empty_strings():
        run_test(True, "")
