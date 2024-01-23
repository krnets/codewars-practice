import codewars_test as test
from kata import cartesian_neighbor


@test.describe("Basic Tests")
def basic_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(
            sorted(cartesian_neighbor(2, 2)),
            [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)],
        )
        test.assert_equals(
            sorted(cartesian_neighbor(0, 0)),
            [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)],
        )
        test.assert_equals(
            sorted(cartesian_neighbor(-5, -5)),
            [
                (-6, -6),
                (-6, -5),
                (-6, -4),
                (-5, -6),
                (-5, -4),
                (-4, -6),
                (-4, -5),
                (-4, -4),
            ],
        )
        test.assert_equals(
            sorted(cartesian_neighbor(-17, 7)),
            [
                (-18, 6),
                (-18, 7),
                (-18, 8),
                (-17, 6),
                (-17, 8),
                (-16, 6),
                (-16, 7),
                (-16, 8),
            ],
        )
