using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static string Unlock(string str)
    {
        var map = new Dictionary<char, int>();
        var keys = new[] {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

        for (int i = 0; i < keys.Length; i++)
            for (int j = 0; j < keys[i].Length; j++)
                map[keys[i][j]] = i;

        return string.Concat(str.ToLower().Select(c => map[c]));
    }
}