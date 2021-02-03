/*
using System.Collections.Generic;
using System.Linq;
using static System.Linq.Enumerable;
using static System.String;

public class Pattern
{
    public static string UpturnNumeralTriangle(int n)
    {
        var list = new List<string>();

        for (int i = 0; i < n; i++)
        {
            var row = new string(' ', i + 1) + Join(' ', Repeat((i + 1) % 10, n - i));
            list.Add(row);
        }

        var rows = Range(0, n).Select(i => new string(' ', i + 1) + Join(' ', Repeat((i + 1) % 10, n - i)));

        return Join('\n', rows);
    }
}
*/

using System.Linq;
using static System.Linq.Enumerable;
using static System.String;

public class Pattern
{
    public static string UpturnNumeralTriangle(int n)
    {
        // return Join('\n', Range(0, n).Select(i => new string(' ', i + 1) + Join(' ', Repeat((i + 1) % 10, n - i))));
        return Join('\n', Range(1, n).Select(i => new string(' ', i) + Join(' ', Repeat(i % 10, n - i + 1))));
    }
}