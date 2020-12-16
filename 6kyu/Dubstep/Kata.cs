using System;
using System.Text.RegularExpressions;

public class Dubstep
{
    public static string SongDecoder(string input)
    {
        // return Regex.Replace(input, "(WUB)+", " ").TrimStart().TrimEnd();
        // return Regex.Replace(input, "(WUB)+", " ").Trim();
        return string.Join(" ", input.Split("WUB", StringSplitOptions.RemoveEmptyEntries));
    }
}