using System;
using System.Collections.Generic;
using System.Linq;

public class SumDigPower
{
    public static long[] SumDigPow(long a, long b)
    {
        var list = new List<long>();

        while (a < b)
        {
            long sum = a.ToString().Select((c, i) => (long) Math.Pow(c - '0', i + 1)).Sum();
            if (sum == a) list.Add(a);
            a++;
        }

        return list.ToArray();
    }
}