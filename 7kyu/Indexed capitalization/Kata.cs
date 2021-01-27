/*
using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static string Capitalize(string s, List<int> idxs)
    {
        return string.Concat(Enumerable.Range(0, s.Length)
            .Select(i => idxs.Contains(i) ? char.ToUpper(s[i]) : s[i]));
    }
}
            */

/*using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static string Capitalize(string s, List<int> idxs)
    {
        return string.Concat(s.Select((c, i) => idxs.Contains(i) ? char.ToUpper(c) : c));
    }
}*/

using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static string Capitalize(string s, List<int> idxs)
    {
        var array = s.ToCharArray();

        foreach (var i in idxs.Where(x => x < s.Length))
            array[i] = char.ToUpper(array[i]);

        return new string(array);
    }
}