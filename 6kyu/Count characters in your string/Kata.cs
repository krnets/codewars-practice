/*using System.Collections.Generic;

public class Kata
{
    public static Dictionary<char, int> Count(string str)
    {
        var map = new Dictionary<char, int>();

        foreach (char c in str)
            if (map.ContainsKey(c))
                map[c]++;
            else map[c] = 1;

        return map;
    }
}*/

using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static Dictionary<char, int> Count(string str)
    {
        return str.GroupBy(c => c).ToDictionary(g => g.Key, g => g.Count());
    }
}