/*
using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static string High(string s)
    {
        string[] words = s.Split(" ");
        List<int> scores = words.Select(w => w.Select(c => c - 'a' + 1).Sum()).ToList();
        int highest = scores.Max();

        return words[scores.IndexOf(highest)];
    }
}
*/

using System.Linq;

public class Kata
{
    public static string High(string s)
    {
        return s.Split(' ').OrderByDescending(w => w.Sum(c => c - 'a' + 1)).First();
    }
}