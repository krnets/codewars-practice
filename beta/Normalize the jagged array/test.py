from kata import normalize
import codewars_test as test


@test.describe("normalize the array")
def tests_():

    tests = (
        # first test
        [[1, 2, 3], [2]],
        # second test
        [[1, 4, 2, 6, 7, 2], [3, 1, 4], [8, 9, 4, 4, 0, 9, 8]],
        # third test
        [[1, 2, 3], [1, 2, 3], [1]],
        # fourth test
        [],
    )

    answers = (
        # first answer
        [[1, 2, 3], [2, None, None]],
        # second answer
        [
            [1, 4, 2, 6, 7, 2, None],
            [3, 1, 4, None, None, None, None],
            [8, 9, 4, 4, 0, 9, 8],
        ],
        # third answer
        [[1, 2, 3], [1, 2, 3], [1, None, None]],
        # fourth answer
        [],
    )

    @test.it("should return properly normalized array (value is None)")
    def fixed_tests():
        for i in range(len(tests)):
            inp = tests[i]
            should_equal = answers[i]
            test.assert_equals(normalize(inp), should_equal)

    @test.it("should return properly normalized array (value is a string)")
    def fixed_tests1():
        inp = [[1, 2, 3], [1]]

        should_equal = [[1, 2, 3], [1, "abc", "abc"]]

        test.assert_equals(normalize(inp, "abc"), should_equal)
