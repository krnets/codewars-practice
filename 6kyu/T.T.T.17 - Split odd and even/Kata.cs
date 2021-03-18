/*
using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static long[] SplitOddAndEven(long n)
    {
        var digits = $"{n}".Select(c => (int) char.GetNumericValue(c));
        var prev = int.MinValue;
        var s = string.Empty;
        var list = new List<string>();

        foreach (var i in digits)
        {
            int curr = i % 2;

            if (curr != prev && s.Length > 0)
            {
                list.Add(s);
                s = $"{i}";
            }
            else s = $"{s}{i}";

            prev = curr;
        }

        list.Add(s);

        return list.Select(long.Parse).ToArray();
    }
}
*/

/*
using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static long[] SplitOddAndEven(long n)
    {
        return Regex.Matches(n.ToString(), @"((?<odd>[13579]+)|(?<even>[2468]+))")
            .SelectMany(match => match.Captures.Select(capture => capture.Value)
                .Select(long.Parse))
            .ToArray();
    }
}
*/

using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static long[] SplitOddAndEven(long n)
    {
        return Regex.Matches(n.ToString(), @"[13579]+|[2468]+").Select(m => long.Parse(m.Value)).ToArray();
    }
}