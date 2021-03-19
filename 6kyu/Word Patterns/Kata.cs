using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static bool WordPattern(string pattern, string str)
    {
        var words = str.Split();

        if ((words.Distinct().Count() != pattern.Distinct().Count()) || words.Length != pattern.Length)
            return false;

        var map = new Dictionary<char, string>();

        for (int i = 0; i < pattern.Length; i++)
        {
            if (!map.ContainsKey(pattern[i]))
                map.Add(pattern[i], words[i]);

            else if (map[pattern[i]] != words[i])
                return false;
        }

        return true;
    }
}