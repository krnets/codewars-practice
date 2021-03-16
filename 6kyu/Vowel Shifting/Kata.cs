using System;
using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string VowelShift(string text, int n)
    {
        if (string.IsNullOrEmpty(text)) return text;

        string vowels, str = Regex.Replace(text, "[^aeiou]", "", RegexOptions.IgnoreCase);
        int i = 0;
        bool neg = n < 0;
        n = Math.Abs(n) % str.Length;

        if (neg)
            vowels = str[n..] + str[..n];
        else vowels = str[^n..] + str[..^n];

        return string.Concat(text.Select(c => vowels.Contains(c) ? vowels[i++] : c));
    }
}