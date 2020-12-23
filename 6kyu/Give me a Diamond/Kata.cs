/*using System.Text;

public class Diamond
{
    public static string print(int n)
    {
        if (n < 0 || n % 2 == 0) return null;

        var sb = new StringBuilder();

        for (int i = 1; i <= n; i += 2)
            sb.Append(' ', (n - i) / 2).Append('*', i).Append('\n');

        for (int i = n - 2; i >= 1; i -= 2)
            sb.Append(' ', (n - i) / 2).Append('*', i).Append('\n');

        return sb.ToString();
    }
}*/

using System;
using System.Text;

public class Diamond
{
    public static string print(int n)
    {
        if (n < 0 || n % 2 == 0) return null;

        var sb = new StringBuilder();
        int mid = n / 2;

        for (int i = 0; i < n; i++)
        {
            int offset = Math.Abs(mid - i);
            sb.Append(' ', offset).Append('*', n - offset * 2).Append('\n');
        }

        return sb.ToString();
    }
}