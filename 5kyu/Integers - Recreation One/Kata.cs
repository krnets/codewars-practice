using System;
using System.Collections.Generic;
using System.Linq;

public class SumSquaredDivisors
{
    private static readonly Dictionary<long, long> SumSquares = new Dictionary<long, long>();

    public static string listSquared(long m, long n)
    {
        var list = new List<List<long>>();

        for (var i = m; i < n; i++)
        {
            var ds = GetDivisorsSum(i);

            if (Math.Sqrt(ds) % 1 == 0)
                list.Add(new List<long>() {i, ds});
        }

        return "[" + string.Join(", ", list.Select(l => $"[{string.Join(", ", l)}]")) + "]";
    }

    private static long GetDivisorsSum(long n)
    {
        if (!SumSquares.ContainsKey(n))
            SumSquares[n] = Enumerable.Range(1, (int) n).Where(i => n % i == 0).Sum(x => x * x);

        return SumSquares[n];
    }
}