/*
using System;
using System.Linq;

public class Kata
{
    public string Convert(string input, string source, string target)
    {
        string str = string.Empty;
        long num = input.Select((c, i) => source.IndexOf(c) * (long) Math.Pow(source.Length, input.Length - 1 - i)).Sum();

        while (num > 0)
        {
            str = target[(int) (num % target.Length)] + str;
            num = num / target.Length;
        }

        return str.Length > 0 ? str : target[0].ToString();
    }
}
*/

public class Kata
{
    public string Convert(string input, string source, string target)
    {
        var str = string.Empty;
        var num = 0L;

        foreach (var c in input)
            num = num * source.Length + source.IndexOf(c);

        while (num > 0)
        {
            str = target[(int) (num % target.Length)] + str;
            num = num / target.Length;
        }

        return str.Length > 0 ? str : target[0].ToString();
    }
}

public class Alphabet
{
    public const string BINARY = "01";
    public const string OCTAL = "01234567";
    public const string DECIMAL = "0123456789";
    public const string HEXA_DECIMAL = "0123456789abcdef";
    public const string ALPHA_LOWER = "abcdefghijklmnopqrstuvwxyz";
    public const string ALPHA_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    public const string ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    public const string ALPHA_NUMERIC = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
}