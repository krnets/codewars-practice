using System;
using System.Linq;

public static class Kata
{
    public static long SumCubes(int n)
    {
        // return (long) Enumerable.Range(1, n).Sum(i => Math.Pow(i, 3));
        // return Enumerable.Range(1, n).Sum(i => (long) Math.Pow(i, 3));
        return Enumerable.Range(1, n).Sum(i => 1L * i * i * i);
        // return (long) Math.Pow(n * (n + 1) / 2, 2);
    }
}