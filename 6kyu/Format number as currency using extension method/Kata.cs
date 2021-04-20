using System;

public static class Kata
{
    public static string ToCurrency(this decimal amount, string prefix)
    {
        var sign = amount < 0 ? "-" : "";

        return $"{sign}{prefix}{Math.Abs(amount):F2}";
    }
}