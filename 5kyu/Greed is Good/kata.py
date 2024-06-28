import codewars_test as test


def score(dice):
    counts = [0] * 7

    for throw in dice:
        counts[throw] += 1

    return (
        (counts[1] // 3 * 1000 + counts[1] % 3 * 100)
        + counts[2] // 3 * 200
        + counts[3] // 3 * 300
        + counts[4] // 3 * 400
        + (counts[5] // 3 * 500 + counts[5] % 3 * 50)
        + counts[6] // 3 * 600
    )


@test.describe("Example Tests")
def example_tests():

    @test.it("Example cases")
    def example_cases():
        test.assert_equals(score([5, 1, 3, 4, 1]), 250)
        test.assert_equals(score([1, 1, 1, 3, 1]), 1100)
        test.assert_equals(score([2, 3, 4, 6, 2]), 0)
        test.assert_equals(score([4, 4, 4, 3, 3]), 400)
        test.assert_equals(score([2, 4, 4, 5, 4]), 450)
