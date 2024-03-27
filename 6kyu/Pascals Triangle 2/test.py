import codewars_test as test
from kata import pascal


@test.describe("Pascal's Triangle #2")
def pascal_triangle_tests():

    @test.describe("Sample tests")
    def sample_tests():
        @test.it("pascal(1)")
        def first_sample():
            test.assert_equals(pascal(1), [[1]])

        @test.it("pascal(2)")
        def first_sample():
            test.assert_equals(pascal(2), [[1], [1, 1]])

        @test.it("pascal(3)")
        def first_sample():
            test.assert_equals(pascal(3), [[1], [1, 1], [1, 2, 1]])

        @test.it("pascal(4)")
        def first_sample():
            test.assert_equals(pascal(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

        @test.it("pascal(5)")
        def second_sample():
            test.assert_equals(
                pascal(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
            )

        @test.it("pascal(6)")
        def second_sample():
            test.assert_equals(
                pascal(6),
                [
                    [1],
                    [1, 1],
                    [1, 2, 1],
                    [1, 3, 3, 1],
                    [1, 4, 6, 4, 1],
                    [1, 5, 10, 10, 5, 1],
                ],
            )

        @test.it("pascal(7)")
        def second_sample():
            test.assert_equals(
                pascal(7),
                [
                    [1],
                    [1, 1],
                    [1, 2, 1],
                    [1, 3, 3, 1],
                    [1, 4, 6, 4, 1],
                    [1, 5, 10, 10, 5, 1],
                    [1, 6, 15, 20, 15, 6, 1],
                ],
            )

        @test.it("pascal(8)")
        def second_sample():
            test.assert_equals(
                pascal(8),
                [
                    [1],
                    [1, 1],
                    [1, 2, 1],
                    [1, 3, 3, 1],
                    [1, 4, 6, 4, 1],
                    [1, 5, 10, 10, 5, 1],
                    [1, 6, 15, 20, 15, 6, 1],
                    [1, 7, 21, 35, 35, 21, 7, 1],
                ],
            )

        @test.it("pascal(9)")
        def second_sample():
            test.assert_equals(
                pascal(9),
                [
                    [1],
                    [1, 1],
                    [1, 2, 1],
                    [1, 3, 3, 1],
                    [1, 4, 6, 4, 1],
                    [1, 5, 10, 10, 5, 1],
                    [1, 6, 15, 20, 15, 6, 1],
                    [1, 7, 21, 35, 35, 21, 7, 1],
                    [1, 8, 28, 56, 70, 56, 28, 8, 1],
                ],
            )

        @test.it("pascal(10)")
        def second_sample():
            test.assert_equals(
                pascal(10),
                [
                    [1],
                    [1, 1],
                    [1, 2, 1],
                    [1, 3, 3, 1],
                    [1, 4, 6, 4, 1],
                    [1, 5, 10, 10, 5, 1],
                    [1, 6, 15, 20, 15, 6, 1],
                    [1, 7, 21, 35, 35, 21, 7, 1],
                    [1, 8, 28, 56, 70, 56, 28, 8, 1],
                    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
                ],
            )

        @test.it("pascal(11)")
        def second_sample():
            test.assert_equals(
                pascal(11),
                [
                    [1],
                    [1, 1],
                    [1, 2, 1],
                    [1, 3, 3, 1],
                    [1, 4, 6, 4, 1],
                    [1, 5, 10, 10, 5, 1],
                    [1, 6, 15, 20, 15, 6, 1],
                    [1, 7, 21, 35, 35, 21, 7, 1],
                    [1, 8, 28, 56, 70, 56, 28, 8, 1],
                    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
                    [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1],
                ],
            )

        @test.it("pascal(12)")
        def second_sample():
            test.assert_equals(
                pascal(12),
                [
                    [1],
                    [1, 1],
                    [1, 2, 1],
                    [1, 3, 3, 1],
                    [1, 4, 6, 4, 1],
                    [1, 5, 10, 10, 5, 1],
                    [1, 6, 15, 20, 15, 6, 1],
                    [1, 7, 21, 35, 35, 21, 7, 1],
                    [1, 8, 28, 56, 70, 56, 28, 8, 1],
                    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
                    [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1],
                    [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1],
                ],
            )
