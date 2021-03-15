using System;
using System.Linq;

public class SqNum
{
    public static long solve(long n)
    {
        return Enumerable.Range(1, (int) n)
            .Select(i => (long) i * i)
            .Where(i => Math.Sqrt(i + n) % 1 == 0)
            .DefaultIfEmpty(-1)
            .First();
    }
}

/*
public class SqNum
{
    public static long solve(long n)
    {
        for (long i = 1; i <= n / 2; i++)
            if (Math.Sqrt(n + (i * i)) % 1 == 0)
                return i * i;

        return -1;
    }
}
*/

/*public class SqNum
{
    public static long solve(long n)
    {
        var ans = long.MaxValue;

        for (long i = 1; i < Math.Sqrt(n); i++)

            if (n % i == 0)
            {
                var x = n / i;

                if ((x - i != 0) && ((x - i) % 2 == 0))
                    ans = Math.Min(ans, (x - i) / 2);
            }

        return ans != long.MaxValue ? ans * ans : -1;
    }
}*/