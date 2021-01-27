/*using System;
using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static List<int> Solve(List<string> arr)
    {
        var alphabetStrings = arr.Select(s => s.Length)
            .Select(i => string.Concat(Enumerable.Range(0, i)
                .Select(j => Convert.ToChar('a' + j))))
            .ToList();

        return arr.Select((word, i) => word.ToLower()
                .Where((c, j) => c.Equals(alphabetStrings[i][j]))
                .Count())
            .ToList();
    }
}*/

using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static List<int> Solve(List<string> arr)
    {
        // return arr.Select(str => str.Where((c, i) => c % 32 == i + 1).Count()).ToList();
        return arr.Select(str => str.Where((c, i) => char.ToLower(c) - 'a' == i).Count()).ToList();
    }
}