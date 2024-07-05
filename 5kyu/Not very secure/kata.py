import re
import codewars_test as test
from string import ascii_letters, digits


# def alphanumeric(password):
#     valid_chars = set(ascii_letters + digits)
#     for c in password:
#         if c not in valid_chars:
#             return False
#     return len(password) > 0


# def alphanumeric(password):
#     valid_chars = set(ascii_letters + digits)
#     return bool(password) and all(c in valid_chars for c in password)


def alphanumeric(password):
    return bool(re.fullmatch(r"[a-z\d]+", password, re.I))


@test.describe("Sample Tests")
def sample_tests():
    tests = [("hello world_", False), ("PassW0rd", True), ("     ", False)]
    for s, b in tests:

        @test.it('alphanumeric("' + s + '")')
        def sample_test():
            test.assert_equals(alphanumeric(s), b)
