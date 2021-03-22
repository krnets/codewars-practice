/*public class SystemOfEq
{
    public static int Solution(int n, int m)
    {
        var ans = 0;

        for (int a = 0; a * a <= n; a++)
        {
            for (int b = 0; b * b <= m; b++)
                if (a * a + b == n && a + b * b == m)
                    ans++;
        }

        return ans;
    }
}*/

using System;
using System.Linq;

public class SystemOfEq
{
    public static int Solution(int n, int m)
    {
        return Enumerable.Range(0, (int) Math.Sqrt(n) + 1).Count(i => Math.Pow((n - i * i), 2) == m - i);
    }
}