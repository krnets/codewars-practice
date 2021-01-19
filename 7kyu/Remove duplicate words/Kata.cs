/*using System.Collections.Generic;

public static class Kata
{
    public static string RemoveDuplicateWords(string s)
    {
        var list = new List<string>();

        foreach (var str in s.Split())
            if (!list.Contains(str))
                list.Add(str);

        return string.Join(' ', list);
    }
}*/

using System.Linq;

public static class Kata
{
    public static string RemoveDuplicateWords(string s)
    {
        return string.Join(" ", s.Split().Distinct());
    }
}