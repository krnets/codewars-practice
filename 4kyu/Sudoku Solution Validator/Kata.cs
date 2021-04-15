using System.Linq;

public class Sudoku
{
    public static bool ValidateSolution(int[][] board)
    {
        return Enumerable.Range(0, 9)
            .SelectMany(row => Enumerable.Range(0, 9)
                .Select(col => $"{row / 3}{col / 3}{board[row][col]}"))
            .Distinct().Count() == 9 * 9;
    }
}