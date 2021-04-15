using System;
using System.Collections.Generic;
using System.Linq;

public class PowerSumDig
{
    public static long PowerSumDigTerm(int n)
    {
        var list = new List<long>();

        for (int i = 2; i < 70; i++)
        {
            for (int j = 2; j < 10; j++)
            {
                var candidate = (long) Math.Pow(i, j);

                if (DigitSum(candidate) == i)
                    list.Add(candidate);
            }
        }

        return list.OrderBy(x => x).ElementAt(n - 1);
    }

    private static long DigitSum(long n)
    {
        long result = 0;

        while (n != 0)
        {
            result = result + n % 10;
            n /= 10;
        }

        return result;
    }
}