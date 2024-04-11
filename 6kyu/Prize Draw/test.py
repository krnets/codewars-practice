import codewars_test as test
from kata import rank


@test.describe("Rank")
def _():
    @test.it("Basic Tests")
    def _():
        test.assert_equals(
            rank("COLIN,AMANDBA,AMANDAB,CAROL,Paul,JOSEPH", [1, 4, 4, 5, 2, 1], 4),
            "Paul",
        )
        test.assert_equals(
            rank(
                "Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin",
                [4, 2, 1, 4, 3, 1, 2],
                4,
            ),
            "Benjamin",
        )
        test.assert_equals(
            rank(
                "Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", [1, 3, 5, 5, 3, 6], 2
            ),
            "Matthew",
        )
        test.assert_equals(
            rank("Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth", [3, 1, 4, 4, 3, 2], 4),
            "Abigail",
        )
        test.assert_equals(rank("Lagon,Lily", [1, 5], 2), "Lagon")
