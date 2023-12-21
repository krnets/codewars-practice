import codewars_test as test
from kata import declare_winner, Fighter


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"), "Lew"
        )

        test.assert_equals(
            declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Harry"),
            "Harry",
        )

        test.assert_equals(
            declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"),
            "Harald",
        )

        test.assert_equals(
            declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"),
            "Harald",
        )

        test.assert_equals(
            declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"),
            "Harald",
        )

        test.assert_equals(
            declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"),
            "Harald",
        )