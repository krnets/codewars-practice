/*using System.Linq;

public static class Kata
{
    public static int[] Capitals(string word)
    {
        return Enumerable.Range(0, word.Length)
            .Where(i => char.IsUpper(word[i]))
            .ToArray();
    }
}*/

/*using System.Linq;

public static class Kata
{
    public static int[] Capitals(string word)
    {
        return word
            .Select((c, index) => new {c, index})
            .Where(_ => char.IsUpper(_.c))
            .Select(_ => _.index)
            .ToArray();
    }
}*/

using System.Linq;

public static class Kata
{
    public static int[] Capitals(string word)
    {
        return word.Select((_, i) => i)
            .Where((_, i) => char.IsUpper(word, i))
            .ToArray();
    }
}

/*using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static int[] Capitals(string word)
    {
        return Regex.Matches(word, "[A-Z]")
            .Select(m => m.Index)
            .ToArray();
    }
}*/