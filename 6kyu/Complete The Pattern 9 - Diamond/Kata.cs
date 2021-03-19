using System.Collections.Generic;
using System.Linq;

public class Diamond
{
    public static string Pattern(int n)
    {
        var list = new List<string>();

        for (int i = 1; i <= n; i++)
        {
            var up = string.Concat(Enumerable.Range(1, i).Select(j => j % 10));
            var down = string.Concat(up.SkipLast(1).Reverse());
            var pad = new string(' ', n - i);
            list.Add($"{pad}{up}{down}{pad}");
        }

        return string.Join("\n", list.Concat(list.SkipLast(1).Reverse().ToList()));
    }
}