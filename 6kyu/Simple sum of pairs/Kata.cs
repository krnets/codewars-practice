using System;
using System.Linq;

public class Solution
{
    public static int solve(long n)
    {
        if (n == 0 || n == 1) return (int) n;

        var length = (int) Math.Floor(Math.Log10(n));
        var b = new string('9', length);
        var x = n - long.Parse(b);

        return (int) x.ToString().Sum(char.GetNumericValue) + 9 * length;
    }
}