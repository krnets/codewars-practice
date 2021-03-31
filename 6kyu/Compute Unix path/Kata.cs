/*using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string CombinePathsUri(params string[] PathParts)
    {
        var cleanedUp = PathParts.SelectMany(s => Regex.Replace(s, @"(\\)|(/)", " ").Split().Where(x => x.Length > 0));

        return "/" + string.Join("/", cleanedUp);
    }
}*/


using System;
using System.Linq;

public class Kata
{
    public static string CombinePathsUri(params string[] PathParts)
    {
        return PathParts.SelectMany(s => s.Split(new[] {"\\", "/", " "}, StringSplitOptions.RemoveEmptyEntries))
            .Aggregate("/", (a, b) => a == "/" ? $"{a}{b}" : $"{a}/{b}");
    }
}