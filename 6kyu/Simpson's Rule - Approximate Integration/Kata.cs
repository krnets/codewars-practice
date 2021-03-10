using System;
using System.Linq;

public class SimpsonIntegration
{
    private static double Fn(double num) => 1.5 * Math.Pow(Math.Sin(num), 3);

    public static double Simpson(int n)
    {
        var h = Math.PI / n;

        return 2 * h * (2 * Enumerable.Range(1, n / 2).Sum(i => Fn((2 * i - 1) * h)) +
                        Enumerable.Range(1, n / 2 - 1).Sum(i => Fn(2 * i * h))) / 3;
    }
}