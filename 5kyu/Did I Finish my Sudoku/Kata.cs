/*using System.Collections.Generic;
using System.Linq;

public class Sudoku
{
    public static string DoneOrNot(int[][] board)
    {
        var set = new HashSet<string>();

        for (int row = 0; row < 9; row++)
        {
            for (int col = 0; col < 9; col++)
                set.Add($"{row / 3},{col / 3}:{board[row][col]}");
        }

        return board.Select(row => row.Length).Sum() == set.Count ? "Finished!" : "Try again!";
    }
}*/

using System.Linq;
using static System.Linq.Enumerable;

public class Sudoku
{
    public static string DoneOrNot(int[][] board)
    {
        return Range(0, 9).SelectMany(row => Range(0, 9).Select(col => $"{row / 3}{col / 3}{board[row][col]}"))
            .Distinct().Count() == 9 * 9
            ? "Finished!"
            : "Try again!";
    }
}