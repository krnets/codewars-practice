import codewars_test as test
from kata import chess_board


@test.describe("Basic tests")
def basic_tests():

    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(chess_board(1, 1), [["O"]])
        test.assert_equals(chess_board(1, 2), [["O", "X"]])
        test.assert_equals(chess_board(2, 1), [["O"], ["X"]])
        test.assert_equals(chess_board(2, 2), [["O", "X"], ["X", "O"]])
        test.assert_equals(
            chess_board(6, 6),
            [
                ["O", "X", "O", "X", "O", "X"],
                ["X", "O", "X", "O", "X", "O"],
                ["O", "X", "O", "X", "O", "X"],
                ["X", "O", "X", "O", "X", "O"],
                ["O", "X", "O", "X", "O", "X"],
                ["X", "O", "X", "O", "X", "O"],
            ],
        )
