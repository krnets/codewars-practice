from contextlib import suppress
import codewars_test as test


def matching(arg):
    with suppress(ZeroDivisionError):
        match arg:
            case []: return 0
            case [x]: return int(x)
            case [head, *tail]: return int(head) / int(tail[-1])


@test.describe("Structural Matching")
def tests():
    @test.it("Fixed Tests")
    def tests():
        test.assert_equals(matching(""), None)
        test.assert_equals(matching("0"), None)
        test.assert_equals(matching([]), 0)
        test.assert_equals(matching(["2"]), 2)
        test.assert_equals(matching([0]), 0)
        test.assert_equals(matching([3, 1, "2"]), 1.5)
        test.assert_equals(matching("123"), None)
        test.assert_equals(matching(["0", 0]), None)
        test.assert_equals(matching(["0", 2, "3"]), 0)
