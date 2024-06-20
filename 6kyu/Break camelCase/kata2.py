import re
import codewars_test as test


# def solution(s):
#     ans = ""
#     for c in s:
#         if c.isupper():
#             ans += " " + c
#         else:
#             ans += c
#     return ans


# def solution(s):
#     return "".join(" " + c if c.isupper() else c for c in s)


def solution(s):
    return re.sub(r"([A-Z])", r" \1", s)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(solution("helloWorld"), "hello World")
        test.assert_equals(solution("camelCase"), "camel Case")
        test.assert_equals(solution("breakCamelCase"), "break Camel Case")
