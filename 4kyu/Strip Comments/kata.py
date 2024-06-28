from itertools import takewhile
from typing import List
import codewars_test as test


# def strip_comments(strng: str, markers: List[str]) -> str:
#     res = []

#     for line in strng.splitlines():
#         res.append("".join(takewhile(lambda c: c not in markers, line)).rstrip())

#     return "\n".join(res)


# def strip_comments(strng, markers):
#     return "\n".join(
#         "".join(takewhile(lambda c: c not in markers, line)).rstrip()
#         for line in strng.splitlines()
#     )


def strip_comments(strng: str, markers: List[str]) -> str:
    parts = []
    for line in strng.splitlines():
        for c in line:
            if c in markers:
                line = line.split(c)[0].rstrip()
                break
        parts.append(line)
    return "\n".join(parts)


@test.describe("Test case")
def test_group():
    @test.it("Example")
    def test_case():
        test.assert_equals(
            strip_comments(
                "apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]
            ),
            "apples, pears\ngrapes\nbananas",
        )
        test.assert_equals(strip_comments("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
        test.assert_equals(strip_comments(" a #b\nc\nd $e f g", ["#", "$"]), " a\nc\nd")
