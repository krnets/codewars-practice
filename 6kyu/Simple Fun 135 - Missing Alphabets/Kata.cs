using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public string MissingAlphabets(string s)
    {
        var sCharCount = s.GroupBy(c => c).ToDictionary(g => g.Key, g => g.Count());
        int charMax = sCharCount.Max(p => p.Value);

        var missingChars = Enumerable.Range(0, 26)
            .Select(i => (char) ('a' + i))
            .Select(c => new string(c, charMax - sCharCount.GetValueOrDefault(c, 0)));

        return string.Concat(missingChars);
    }
}