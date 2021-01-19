using System;

public static class Kata
{
    public static Func<double, double> Add(double n)
    {
        return m => m + n;
    }
}