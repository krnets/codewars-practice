/*using System;

public class Suite
{
    public static double going(int n)
    {
        double total = 1, acc = 1, d;

        for (int i = n; i > 1; i--)
        {
            acc *= i;
            d = 1 / acc;
            if (Math.Round(d, 6) == 0) break;
            total += d;
        }

        return double.Parse($"{total:F8}"[..8]);
    }
}*/

using System;

public class Suite
{
    public static double going(int n)
    {
        double res = 1, acc = 1, p = Math.Pow(10, 6);

        for (double d = n; d > 1; d--)
        {
            acc *= 1 / d;
            res += acc;
        }

        return Math.Floor(res * p) / p;
    }
}