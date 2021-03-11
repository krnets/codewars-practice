/*using System;
using System.Linq;
using System.Text.RegularExpressions;

public class Cubes
{
    public static string isSumOfCubes(string s)
    {
        s = Regex.Replace(s, "\\D", " ");

        var cubicNums = Regex.Split(s, "\\s+")
            .SelectMany(ss => Regex.Split(ss, @"(?<=\G.{3})")
                .Where(str => str.Length > 0)
                .Select(int.Parse))
            .Where(IsCubic).ToArray();

        return cubicNums.Any() ? $"{string.Join(" ", cubicNums)} {cubicNums.Sum()} Lucky" : "Unlucky";
    }

    private static bool IsCubic(int n)
    {
        return n == (int) n.ToString().Sum(c => Math.Pow(char.GetNumericValue(c), 3));
    }
}*/

using System;
using System.Linq;
using System.Text.RegularExpressions;

public class Cubes
{
    public static string isSumOfCubes(string s)
    {
        var cubicNums = Regex.Matches(s, @"\d{1,3}")
            .Select(m => int.Parse(m.Value))
            .Where(n => n.ToString().Sum(c => Math.Pow(char.GetNumericValue(c), 3)) == n)
            .ToArray();

        return cubicNums.Any() ? $"{string.Join(" ", cubicNums)} {cubicNums.Sum()} Lucky" : "Unlucky";
    }
}

/*using System;
using System.Linq;
using System.Text.RegularExpressions;

public class Cubes
{
    public static string isSumOfCubes(string s)
    {
        var cubicNums = Regex.Matches(s, @"\d{1,3}")
            .Select(m => int.Parse(m.Value))
            .Where(n => n.ToString().Sum(c => Math.Pow(char.GetNumericValue(c), 3)) == n)
            .ToArray();

        return cubicNums.Any() ? cubicNums.Aggregate("", (str, n) => $"{str}{n} ") + cubicNums.Sum() + " Lucky" : "Unlucky";
    }
}*/