using System.Linq;

public static class Kata
{
    public static string Transform(string s)
    {
        var charCount = s.GroupBy(c => c).ToDictionary(g => g.Key, g => g.Count());

        return string.Concat(s.Distinct().Select(c => charCount[c] > 1 ? $"{c}{charCount[c]}" : $"{c}"));
    }
}