import codewars_test as test
from kata import stat


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"),
            "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34",
        )
        test.assert_equals(
            stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"),
            "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00",
        )
        test.assert_equals(
            stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|32|34, 2|17|17"),
            "Range: 00|31|17 Average: 02|27|10 Median: 02|24|57",
        )
        test.assert_equals(
            stat("0|15|59, 0|16|16, 0|17|20, 0|22|34, 0|19|34, 0|15|0"),
            "Range: 00|07|34 Average: 00|17|47 Median: 00|16|48",
        )
        test.assert_equals(
            stat(
                "11|15|59, 10|16|16, 12|17|20, 9|22|34, 13|19|34, 11|15|17, 11|22|00, 10|26|37, 12|17|48, 9|16|30, 12|20|14, 11|25|11"
            ),
            "Range: 04|03|04 Average: 11|14|36 Median: 11|18|59",
        )
        test.assert_equals(
            stat(
                "1|15|59, 1|16|16, 1|17|20, 1|22|34, 1|19|34, 1|15|17, 1|22|00, 1|26|37, 1|17|48, 1|16|30, 1|20|14, 1|25|11"
            ),
            "Range: 00|11|20 Average: 01|19|36 Median: 01|18|41",
        )

        test.assert_equals(stat(""), "")
