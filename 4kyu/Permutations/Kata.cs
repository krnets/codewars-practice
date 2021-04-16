/*
using System.Collections.Generic;
using System.Linq;

class Permutations
{
    public static List<string> SinglePermutations(string s)
    {
        var result = new List<List<char>>();

        Permute(s.ToCharArray(), 0, s.Length - 1, result);

        return result.Select(chars => string.Concat(chars)).Distinct().ToList();
    }

    private static void Permute(char[] chars, int start, int end, List<List<char>> list)
    {
        if (start == end)
            list.Add(new List<char>(chars));
        else
            for (var i = start; i <= end; i++)
            {
                (chars[start], chars[i]) = (chars[i], chars[start]);
                Permute(chars, start + 1, end, list);
                (chars[start], chars[i]) = (chars[i], chars[start]);
            }
    }
}
*/

/*using System.Collections.Generic;
using System.Linq;

class Permutations
{
    public static List<string> SinglePermutations(string s)
    {
        return $"{s}".Length < 2
            ? new List<string> {s}
            : SinglePermutations(s[1..])
                .SelectMany(p => Enumerable.Range(0, p.Length + 1)
                    .Select(i => p[..i] + s[0] + p[i..]))
                .Distinct()
                .ToList();
    }
}*/

/*using System.Collections.Generic;
using System.Linq;

class Permutations
{
    public static List<string> SinglePermutations(string s)
    {
        if (s.Length < 2) return new List<string> {s};

        var set = new HashSet<string>();

        foreach (var permutation in SinglePermutations(s[1..]))
        {
            for (int i = 0; i <= permutation.Length; i++)
            {
                set.Add(permutation[..i] + s[0] + permutation[i..]);
            }
        }

        return set.ToList();
    }
}*/

using System.Collections.Generic;
using System.Linq;

class Permutations
{
    public static List<string> SinglePermutations(string s)
    {
        var set = new HashSet<string> {s};

        for (int i = 0; i < s.Length; i++)
            set.UnionWith(SinglePermutations(s.Remove(i, 1)).Select(p => s[i] + p));

        return set.ToList();
    }
}