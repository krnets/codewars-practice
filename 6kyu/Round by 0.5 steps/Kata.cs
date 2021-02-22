using System;

public class Kata
{
    public static double Solution(double n)
    {
        // return ((int) (2 * n + 0.5)) / 2.0;
        return Math.Round(n * 2) / 2.0;
    }
}