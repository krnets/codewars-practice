/*using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string GenerateGroupings(int[] input)
    {
        Array.Sort(input);
        var prev = input.First();
        var list = new List<string> {prev.ToString()};

        foreach (var curr in input.Skip(1))
        {
            if (curr - prev == 0)
                continue;
            if (curr - prev > 1)
                list.Add(list.Last() == "-" ? $"{prev}, {curr}" : $", {curr}");
            else if (curr - prev == 1 && list.Last() != "-")
                list.Add("-");

            prev = curr;
        }

        if (!Regex.IsMatch(list.Last(), $@"(,\s)?{prev}"))
            list.Add($"{prev}");

        return string.Concat(list);
    }
}*/

using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static string GenerateGroupings(int[] input)
    {
        Array.Sort(input);
        var prev = input.First();
        var list = new List<string> {prev.ToString()};

        foreach (var curr in input.Distinct().Skip(1))
        {
            if (curr - prev > 1)
                list.Add(list.Last() == "-" ? $"{prev}, {curr}" : $", {curr}");
            else if (curr - prev == 1 && list.Last() != "-")
                list.Add("-");

            prev = curr;
        }

        if (list.Last() == "-")
            list.Add(prev.ToString());

        return string.Concat(list);
    }
}