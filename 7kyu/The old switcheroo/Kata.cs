/*using System.Linq;

public class Kata
{
    public static string Vowel2Index(string str)
    {
        const string vowels = "aeiou";

        return string.Concat(str.Select((c, i) => vowels.Contains(c) ? $"{i + 1}" : c.ToString()));
    }
}*/

using System.Text.RegularExpressions;

public class Kata
{
    public static string Vowel2Index(string str)
    {
        {
            return Regex.Replace(str, "[aeiou]", m => $"{m.Index + 1}");
        }
    }
}