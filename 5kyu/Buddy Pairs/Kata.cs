using System;
using System.Linq;

public class Bud
{
    public static string Buddy(long start, long limit)
    {
        for (long i = start; i <= limit; i++)
        {
            var m = SumDivisors(i);
            var n = SumDivisors(m);

            if (m > i && n == i)
                return $"({i} {m})";
        }

        return "Nothing";
    }

    public static long SumDivisors(long n)
    {
        return Enumerable.Range(2, (int) Math.Sqrt(n)).Aggregate(0L, (acc, i) => acc + (n % i == 0 ? i + n / i : 0));
    }
}