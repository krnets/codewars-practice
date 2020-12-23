using System;
using System.Linq;

public class Revrot
{
    public static string RevRot(string strng, int sz)
    {
        if (string.IsNullOrEmpty(strng) || sz <= 0 || sz > strng.Length)
            return string.Empty;

        return string.Concat(Enumerable.Range(0, strng.Length / sz)
            .Select(i => strng.Substring(i * sz, sz))
            .Select(chunk => chunk.Select(char.GetNumericValue)
                .Sum(digit => Math.Pow(digit, 3)) % 2 == 0
                ? chunk.Reverse()
                : chunk[1..] + chunk[0])
            .SelectMany(enumerable => enumerable));
    }
}