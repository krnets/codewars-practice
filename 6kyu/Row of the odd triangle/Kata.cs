/*using System;

public class UserSolution
{
    public static long[] OddRow(int n)
    {
        var row = new long[n];
        var val = (long) Math.Pow((n - 1), 2) + n;

        for (int i = 0; i < n; i++)
        {
            row[i] = val;
            val += 2;
        }

        return row;
    }
}*/

using System.Linq;

public class UserSolution
{
    public static long[] OddRow(int n)
    {
        var offset = (long) n * (n - 1) + 1;

        return Enumerable.Range(0, n).Select(i => offset + 2 * i).ToArray();
    }
}