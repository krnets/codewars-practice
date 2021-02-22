using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static Dictionary<string, int> Count(List<string> lst)
    {
        return lst.GroupBy(x => x).ToDictionary(g => g.Key, g => g.Count());
    }
}