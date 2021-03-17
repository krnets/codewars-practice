/*
using System;
using System.Linq;

public class BeforeAfterPrimes
{
    public static long[] PrimeBefAft(long num)
    {
        long a = num - Enumerable.Range(1, (int) num).First(i => IsPrime(num - i));
        long b = num + Enumerable.Range(1, (int) num).First(i => IsPrime(num + i));

        return new[] {a, b};
    }

    private static bool IsPrime(long n)
    {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0) return false;

        for (int i = 5; i <= Math.Sqrt(n); i += 6)
            if (n % i == 0 || n % (i + 2) == 0)
                return false;

        return true;
    }
}
*/


public class BeforeAfterPrimes
{
    public static long[] PrimeBefAft(long num)
    {
        var result = new[] {num - 1, num + 1};

        while (!IsPrime(result[0])) result[0]--;
        while (!IsPrime(result[1])) result[1]++;

        return result;
    }

    private static bool IsPrime(long n)
    {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0) return false;

        for (int i = 5; i * i <= n; i += 6)
            if (n % i == 0 || n % (i + 2) == 0)
                return false;

        return true;
    }
}