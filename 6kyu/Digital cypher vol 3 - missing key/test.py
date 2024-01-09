import codewars_test as test
from kata import find_the_key


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(find_the_key("scout", [20, 12, 18, 30, 21]), 1939)
        test.assert_equals(find_the_key("scoutc", [20, 12, 18, 30, 21, 12]), 1939)
        test.assert_equals(find_the_key("scoutco", [20, 12, 18, 30, 21, 12, 18]), 1939)
        test.assert_equals(
            find_the_key("masterpiece", [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]), 1939
        )
        test.assert_equals(
            find_the_key("nomoretears", [15, 17, 14, 17, 19, 7, 21, 7, 2, 20, 20]), 12
        )
        test.assert_equals(
            find_the_key("tenthousand", [21, 5, 14, 20, 8, 16, 21, 19, 1, 14, 5]), 10000
        )
        test.assert_equals(
            find_the_key(
                "wouldgiveonedifferentown",
                [
                    32,
                    24,
                    29,
                    13,
                    13,
                    16,
                    17,
                    23,
                    14,
                    24,
                    22,
                    6,
                    13,
                    18,
                    14,
                    7,
                    14,
                    27,
                    13,
                    15,
                    29,
                    24,
                    31,
                    15,
                ],
            ),
            9981,
        )
        test.assert_equals(
            find_the_key(
                "firstchildfeellarge",
                [
                    13,
                    16,
                    21,
                    25,
                    27,
                    10,
                    11,
                    15,
                    19,
                    11,
                    9,
                    11,
                    12,
                    19,
                    15,
                    7,
                    25,
                    14,
                    8,
                ],
            ),
            7736,
        )
