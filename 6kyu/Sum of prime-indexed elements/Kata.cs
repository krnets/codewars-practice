using System;
using System.Linq;

public class Solution
{
    public static int solve(int[] arr)
    {
        // return Enumerable.Range(0, arr.Length).Where(IsPrime).Sum(i => arr[i]);
        return arr.Where((_, i) => IsPrime(i)).Sum();
    }

    private static bool IsPrime(int n)
    {
        if (n < 2) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;

        for (int i = 5; i <= Math.Sqrt(n); i += 6)
            if (n % i == 0 || n % (i + 2) == 0)
                return false;

        return true;
    }
}