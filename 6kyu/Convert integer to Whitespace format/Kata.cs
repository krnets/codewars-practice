using System;

public class Kata
{
    public static string WhitespaceNumber(int n)
    {
        // return (n > 0 ? " " : n < 0 ? "\t" : string.Empty) +
        return (n < 0 ? "\t" : n > 0 ? " " : string.Empty) +
               Convert.ToString(Math.Abs(n), 2)
                   .Replace("0", " ")
                   .Replace("1", "\t") + "\n";
    }
}