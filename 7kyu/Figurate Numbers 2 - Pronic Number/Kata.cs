using System;

public class Kata
{
    public static bool IsPronic(int n)
    {
        if (n < 0) return false;
        var x = (int) Math.Sqrt(n);

        return x * (x + 1) == n;
    }
}