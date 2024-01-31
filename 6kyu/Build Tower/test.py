import codewars_test as test
from kata import tower_builder


@test.describe("Build Tower")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            tower_builder(1),
            [
                "*",
            ],
        )
        test.assert_equals(tower_builder(2), [
            " * ", 
            "***"])
        test.assert_equals(tower_builder(3), [
            "  *  ", 
            " *** ", 
            "*****"])
        test.assert_equals(
            tower_builder(4), [
                "   *   ", 
                "  ***  ", 
                " ***** ", 
                "*******"]
        )
        test.assert_equals(
            tower_builder(5),
            ["    *    ", 
             "   ***   ", 
             "  *****  ", 
             " ******* ", 
             "*********"],
        ),
        test.assert_equals(
            tower_builder(6),
            [
                "     *     ",
                "    ***    ",
                "   *****   ",
                "  *******  ",
                " ********* ",
                "***********",
            ],
        ),
        test.assert_equals(
            tower_builder(7),
            [
                "      *      ",
                "     ***     ",
                "    *****    ",
                "   *******   ",
                "  *********  ",
                " *********** ",
                "*************",
            ],
        )
