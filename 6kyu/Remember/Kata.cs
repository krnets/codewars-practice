/*using System.Collections.Generic;

public static class Kata
{
    public static List<char> Remember(string str)
    {
        var seen = new List<char>();
        var dups = new List<char>();

        foreach (char c in str)
            if (seen.Contains(c) && !dups.Contains(c))
                dups.Add(c);
            else seen.Add(c);

        return dups;
    }
}*/

using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static List<char> Remember(string str)
    {
        var seen = new HashSet<char>();

        return str.Where(c => !seen.Add(c)).Distinct().ToList();
    }
}