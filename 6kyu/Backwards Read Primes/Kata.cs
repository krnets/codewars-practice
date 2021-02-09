using System;
using System.Linq;

public class BackWardsPrime
{
    public static string backwardsPrime(long start, long end)
    {
        return string.Join(" ", Enumerable.Range((int) start, (int) (end - start + 1))
            .Where(i => !IsAnagram(i.ToString()))
            .Where(IsPrime)
            .Where(i => IsPrime(int.Parse(string.Concat(i.ToString().Reverse())))));
    }

    private static bool IsAnagram(string str) => str.Reverse().SequenceEqual(str);

    private static bool IsPrime(int n)
    {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;

        for (int i = 3; i <= Math.Sqrt(n); i += 2)
            if (n % i == 0)
                return false;

        return true;
    }
}