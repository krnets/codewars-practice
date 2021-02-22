/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    private static readonly Dictionary<string, int> NumbersMap = new Dictionary<string, int>()
    {
        ["zero"] = 0, ["one"] = 1, ["two"] = 2, ["three"] = 3, ["four"] = 4,
        ["five"] = 5, ["six"] = 6, ["seven"] = 7, ["eight"] = 8, ["nine"] = 9
    };

    public static string AverageString(string str)
    {
        var words = str.Split(' ');

        if (words.Any(w => !NumbersMap.ContainsKey(w)))
            return "n/a";

        int average = words.Sum(w => NumbersMap[w]) / words.Length;

        foreach (var (key, value) in NumbersMap)
            if (value == average)
                return key;

        return "n/a";
    }
}*/

using System;
using System.Linq;

public class Kata
{
    private static readonly string[] Numbers =
        {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    public static string AverageString(string str)
    {
        var words = str.Split();

        if (words.Any(w => !Numbers.Contains(w)))
            return "n/a";

        var average = words.Sum(w => Array.IndexOf(Numbers, w)) / words.Length;

        return Numbers[average];
    }
}