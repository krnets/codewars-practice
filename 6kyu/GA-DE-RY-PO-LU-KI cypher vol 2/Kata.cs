using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string Encode(string str, string key)
    {
        var map = new Dictionary<char, char>();

        foreach ((char first, char second) in Regex.Matches(key, "(..)").Select(m => new Tuple<char, char>(m.Value[0], m.Value[1])))
        {
            map[first] = second;
            map[second] = first;
            map[char.ToUpper(first)] = char.ToUpper(second);
            map[char.ToUpper(second)] = char.ToUpper(first);
        }

        return string.Concat(str.Select(c => map.GetValueOrDefault(c, c)));
    }

    public static string Decode(string str, string key)
    {
        return Encode(str, key);
    }
}