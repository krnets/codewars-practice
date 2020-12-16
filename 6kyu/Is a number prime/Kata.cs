/*using System;

public static class Kata
{
    public static bool IsPrime(int n)
    {
        for (int i = 2; i <= Math.Sqrt(n); i++)
            if (n % i == 0)
                return false;

        return n >= 2;
    }
}*/

using System;

public static class Kata
{
    public static bool IsPrime(int n)
    {
        if (n <= 2 || n % 2 == 0) return n == 2;

        for (int i = 3; i <= Math.Sqrt(n); i += 2)
            if (n % i == 0)
                return false;

        return true;
    }
}