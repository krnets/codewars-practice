using System.Collections.Generic;
using System.Linq;

public class NumberPyramid
{
    public static string Pattern(int n)
    {
        if (n < 1) return string.Empty;
        var rows = new List<string>();

        for (int row = 1; row <= n; row++)
        {
            var ascending = Enumerable.Range(1, row).Select(i => i % 10);
            var descending = ascending.SkipLast(1).Reverse();
            var pad = new string(' ', n - row);
            var s = $"{pad}{string.Concat(ascending.Concat(descending))}{pad}";
            rows.Add(s);
        }

        return string.Join("\n", rows);
    }
}