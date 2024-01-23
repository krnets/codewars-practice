from kata import remove
import codewars_test as test


@test.describe("Tests")
def tests():
    def do_test(input, expected):
        actual = remove(input)
        test.assert_equals(actual, expected, f"for {repr(input)}\n")

    tests = [
        ["Hi!", "Hi!"],
        ["Hi! Hi!", "Hi Hi!!"],
        ["Hi! Hi! Hi!", "Hi Hi Hi!!!"],
        ["Hi! !Hi Hi!", "Hi Hi Hi!!!"],
        ["Hi! Hi!! Hi!", "Hi Hi Hi!!!!"],
    ]

    @test.it("Sample Tests")
    def sample_tests():
        for input, expected in tests:
            do_test(input, expected)
