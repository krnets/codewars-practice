import codewars_test as test


def is_valid_walk(walk):
    x, y = 0, 0
    for step in walk:
        match step:
            case 'n': y += 1
            case 's': y -= 1
            case 'w': x -= 1
            case 'e': x += 1
    return len(walk) == 10 and x == 0 and y == 0



@test.describe("Walk Validator - fixed tests")
def sample_tests():
    @test.it("should return true for a valid walk")
    def _():
        test.assert_equals(
            is_valid_walk(["n", "s", "n", "s", "n", "s", "n", "s", "n", "s"]),
            True,
            "should return True",
        )

    @test.it("should return false if walk is too long")
    def _():
        test.assert_equals(
            is_valid_walk(["w", "e", "w", "e", "w", "e", "w", "e", "w", "e", "w", "e"]),
            False,
            "should return False",
        )

    @test.it("should return false if walk is too short")
    def _():
        test.assert_equals(is_valid_walk(["w"]), False, "should return False")

    @test.it("should return false if walk does not bring you back to start")
    def _():
        test.assert_equals(
            is_valid_walk(["n", "n", "n", "s", "n", "s", "n", "s", "n", "s"]),
            False,
            "should return False",
        )
