using System;

class StepInPrimes
{
    public static long[] Step(int g, long m, long n)
    {
        for (long i = m; i <= n - g; i++)
            if (IsPrime(i) && IsPrime(i + g))
                return new[] {i, i + g};

        return null;
    }

    private static bool IsPrime(long num)
    {
        if (num <= 1) return false;
        if (num <= 3) return true;
        if (num % 2 == 0 || num % 3 == 0) return false;

        for (int i = 5; i <= Math.Sqrt(num); i += 6)
            if (num % i == 0 || num % (i + 2) == 0)
                return false;

        return true;
    }

    /*
    private static bool IsPrime(long num)
    {
        if (num % 2 == 0 && num > 2) return false;
        if (num % 5 == 0 && num > 5) return false;

        for (int i = 3; i <= Math.Sqrt(num); i++)
            if (num % i == 0)
                return false;

        return true;
    }
*/
}