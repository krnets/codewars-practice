using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static IEnumerable<string> MyLanguages(Dictionary<string, int> results)
    {
        return results.Where(pair => pair.Value >= 60).OrderByDescending(p => p.Value).Select(p => p.Key);
    }
}