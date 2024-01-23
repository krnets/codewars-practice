import codewars_test as test
from kata import replace_all


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        tests = (
            (([], 1, 2), []),
            (([1, 2, 2], 1, 2), [2, 2, 2]),
            (([1, 1, 2], 1, 2), [2, 2, 2]),
            (([1, 2, 1, 2, 1], 1, 2), [2, 2, 2, 2, 2]),
            (("Hello World", "o", "0"), "Hell0 W0rld"),
        )

        for t in tests:
            inp, exp = t
            test.assert_equals(replace_all(*inp), exp)
