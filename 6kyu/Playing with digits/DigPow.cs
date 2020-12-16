using System;
using System.Linq;

public class DigPow
{
    public static long digPow(int n, int p)
    {
        long k = Convert.ToInt64(n.ToString().Select(c => Math.Pow(char.GetNumericValue(c), p++)).Sum());

        return k % n == 0 ? k / n : -1;
    }
}