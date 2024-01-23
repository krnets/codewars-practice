import codewars_test as test
from kata import dative


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        tests = [
            # [input, expected],
            ["ablak", "ablaknak"],
            ["tükör", "tükörnek"],
            ["keret", "keretnek"],
            ["otthon", "otthonnak"],
            ["virág", "virágnak"],
            ["tett", "tettnek"],
            ["rokkant", "rokkantnak"],
            ["rossz", "rossznak"],
            ["gonosz", "gonosznak"],
            ["rög", "rögnek"],
            ["király", "királynak"],
        ]

        for inp, exp in tests:
            print("%s -> %s" % (inp, exp))
            test.assert_equals(dative(inp), exp)
