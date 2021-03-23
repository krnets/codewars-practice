/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static string DisplayBoard(char[] board, int width)
    {
        var strip = string.Concat(Enumerable.Repeat('-', 4 * width - 1));
        var lines = new List<string>();

        for (int i = 0; i < board.Length; i += width)
        {
            var cells = new List<string>();

            for (int j = i; j < (i + width); j++)
                cells.Add($" {board[j]} ");

            lines.Add(string.Join("|", cells));
        }

        return string.Join($"\n{strip}\n", lines);
    }
}*/

using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static string DisplayBoard(char[] board, int width)
    {
        var strip = new string('-', 4 * width - 1);
        var lines = new List<string>();

        for (int i = 0; i < board.Length; i += width)
            lines.Add(string.Join("|", board.Skip(i).Take(width).Select(c => $" {c} ")));

        return string.Join($"\n{strip}\n", lines);
    }
}