from kata import vert_mirror, hor_mirror, oper
import codewars_test as test


@test.describe("opstrings")
def fixed_tests():
    @test.it("Basic tests vert_mirror")
    def basic_test_cases_vertical():
        test.assert_equals(
            oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"),
            "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw",
        )

    test.assert_equals(
        oper(vert_mirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"),
        "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP",
    )

    @test.it("Basic tests hor_mirror")
    def basic_test_cases_horizontal():
        test.assert_equals(
            oper(hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"), "yeCt\nCSbg\nJVhv\nlVHt"
        )
        test.assert_equals(
            oper(hor_mirror, "njMK\ndbrZ\nLPKo\ncEYz"), "cEYz\nLPKo\ndbrZ\nnjMK"
        )
