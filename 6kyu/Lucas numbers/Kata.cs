using System;
using System.Collections.Generic;
using System.Linq;

public static class Lucas
{
    public static long lucasnum(int n)
    {
        var seq = new List<long> {2, 1};
        if (n == 0 || n == 1) return seq[n];

        for (int i = 1; i < Math.Abs(n); i++)
            seq.Add(seq[i - 1] + seq[i]);

        return n < 0 && n % 2 != 0 ? -seq.Last() : seq.Last();
    }
}