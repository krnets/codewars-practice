from kata2 import add_letters
import codewars_test as test


@test.describe("Fixed tests")
def fixed_tests():
    tests = [
        (["a", "b", "c"], "f"),
        (["z"], "z"),
        (["a", "b"], "c"),
        (["c"], "c"),
        (["z", "a"], "a"),
        (["y", "c", "b"], "d"),
        ([], "z"),
    ]
    for i, o in tests:
        str = ", ".join(['"' + s + '"' for s in i])

        @test.it("add_letters(" + str + ")")
        def fixed_test():
            test.assert_equals(add_letters(*i), o)
