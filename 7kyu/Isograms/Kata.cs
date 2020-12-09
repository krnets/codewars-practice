/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static bool IsIsogram(string str)
    {
        var map = new Dictionary<char, int>();

        foreach (char c in str.ToLower())
            if (map.ContainsKey(c)) map[c]++;
            else map.Add(c, 1);

        return map.Values.All(x => x == 1);
    }
}*/

/*using System.Linq;

public class Kata
{
    public static bool IsIsogram(string str)
    {
        return str.Length == str.ToLower().Distinct().Count();
    }
}*/

using System.Linq;

public class Kata
{
    public static bool IsIsogram(string str)
    {
        return str.ToLower().GroupBy(c => c).All(x => x.Count() == 1);
    }
}