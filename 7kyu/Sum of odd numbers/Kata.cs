using System;
using System.Linq;

public static class Kata
{
    public static long rowSumOddNumbers(long n)
    {
        // return (long) Math.Pow(n, 3);
        // return n * n * n;
        /*
        return Enumerable.Range(1, (int) (n * n + n))
            .Where(i => i % 2 != 0)
            .Reverse()
            .Take((int) n)
            .Sum();
        */
        return Enumerable.Range((int) (n * (n - 1) + 1), (int) (2 * n))
            .Where(i => i % 2 != 0)
            .Sum();
    }
}