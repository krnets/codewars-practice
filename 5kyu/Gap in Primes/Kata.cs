using System;

class GapInPrimes
{
    public static long[] Gap(int g, long m, long n)
    {
        long prevPrime = 2;

        for (long i = m; i <= n; i++)
            if (IsPrime(i))
                if (i - prevPrime == g)
                    return new[] {prevPrime, i};
                else prevPrime = i;

        return null;
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