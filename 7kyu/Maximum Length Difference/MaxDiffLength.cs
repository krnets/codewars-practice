using System;

public class MaxDiffLength
{
    public static int Mxdiflg(string[] a1, string[] a2)
    {
        if (a1.Length == 0 || a2.Length == 0) return -1;

        int a1Min = Int32.MaxValue;
        int a1Max = Int32.MinValue;

        int a2Min = Int32.MaxValue;
        int a2Max = Int32.MinValue;

        foreach (var str in a1)
        {
            a1Min = Math.Min(str.Length, a1Min);
            a1Max = Math.Max(str.Length, a1Max);
        }

        foreach (var str in a2)
        {
            a2Min = Math.Min(str.Length, a2Min);
            a2Max = Math.Max(str.Length, a2Max);
        }

        return Math.Max(a1Max - a2Min, a2Max - a1Min);
    }
}

/*
using System;
using System.Linq;

public class MaxDiffLength
{
    public static int Mxdiflg(string[] a1, string[] a2)
    {
        return a1.SelectMany(_ => a2, (s1, s2) => Math.Abs(s1.Length - s2.Length))
            .DefaultIfEmpty(-1)
            .Max();
    }
}
*/

/*using System;

public class MaxDiffLength
{
    public static int Mxdiflg(string[] a1, string[] a2)
    {
        int max = -1;

        foreach (string x in a1)
        {
            foreach (string y in a2)
            {
                int diff = Math.Abs(x.Length - y.Length);
                max = Math.Max(diff, max);
            }
        }

        return max;
    }
}*/