using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static int[] Divisors(int n)
    {
        var set = new HashSet<int>();

        for (int i = 2; i <= Math.Sqrt(n); i++)
            if (n % i == 0)
            {
                set.Add(i);
                set.Add(n / i);
            }

        return set.Count == 0 ? null : set.OrderBy(x => x).ToArray();
    }
}