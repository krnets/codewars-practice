/*using System;
using System.Text;

public static class Kata
{
    public static string Performance(Func<int> method)
    {
        var sb = new StringBuilder();
        const int limit = 150_000;

        for (int i = 0; i < limit; i++)
            sb.Append(method.Invoke());

        return sb.ToString();
    }
}*/

using System;
using System.Linq;

public static class Kata
{
    private const int Limit = 150_000;

    public static string Performance(Func<int> method)
    {
        return string.Concat(Enumerable.Range(0, Limit).Select(_ => method()));
    }
}