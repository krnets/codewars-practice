using System;

public class PerfectPower
{
    public static (int, int)? IsPerfectPower(int n)
    {
        var logN = Math.Log(n);

        for (int m = 2; m <= Math.Sqrt(n); m++)
        {
            int k = (int) Math.Round(logN / Math.Log(m));

            if (Math.Pow(m, k) == n)
                return (m, k);
        }

        return null;
    }
}