using System;
using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static int FisHex(string name)
    {
        return Regex.Replace(name, @"[^a-f]", "", RegexOptions.IgnoreCase)
            .Select(c => Convert.ToInt32(c.ToString(), 16))
            .DefaultIfEmpty(0)
            .Aggregate((a, b) => a ^ b);
    }
}