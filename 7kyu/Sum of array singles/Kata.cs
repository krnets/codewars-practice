using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static int Repeats(List<int> source)
    {
        return source.GroupBy(i => i)
            // .ToDictionary(g => g.Key, g => g.Count())
            //.Where(p => p.Value == 1)
            .Where(p => p.Count() == 1)
            .Sum(p => p.Key);
    }
}