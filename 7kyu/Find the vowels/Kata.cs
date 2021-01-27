/*using System.Linq;

public class Kata
{
    private const string Vowels = "aeiouy";

    public static int[] VowelIndices(string word)
    {
        return Enumerable.Range(0, word.Length)
            .Where(i => Vowels.Contains(char.ToLower(word[i])))
            .Select(i => i + 1)
            .ToArray();
    }
}*/

using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    private const string Vowels = "[aeiouy]";

    public static int[] VowelIndices(string word)
    {
        return Regex.Matches(word, Vowels, RegexOptions.IgnoreCase).Select(m => m.Index + 1).ToArray();
    }
}