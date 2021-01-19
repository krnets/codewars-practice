/*using System.Linq;
using System.Text;

public class Kata
{
    public string Pattern(int n)
    {
        if (n < 1) return string.Empty;

        var sb = new StringBuilder();

        for (int i = 1; i <= n; i++)
        {
            var str= string.Concat(Enumerable.Repeat(i, i));
            sb.Append(str).Append('\n');
        }

        return sb.ToString().Trim();
    }
}*/

using System;
using System.Linq;
using static System.String;

public class Kata
{
    public string Pattern(int n)
    {
        //return Join('\n', Enumerable.Range(1, n < 1 ? 0 : n).Select(i => Concat(Enumerable.Repeat(i, i))));
        return Join('\n', Enumerable.Range(1, Math.Max(0, n)).Select(i => Concat(Enumerable.Repeat(i, i))));
    }
}