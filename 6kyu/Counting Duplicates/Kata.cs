/*
using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static int DuplicateCount(string str)
    {
        var map = new Dictionary<char, int>();

        foreach (char c in str.ToLower())
            if (map.ContainsKey(c))
                map[c]++;
            else map[c] = 1;

        return map.Values.Count(x => x > 1);
    }
}
*/

using System.Linq;

public class Kata
{
    public static int DuplicateCount(string str)
    {
        return str.ToLower().GroupBy(c => c).Count(g => g.Count() > 1);
    }
}