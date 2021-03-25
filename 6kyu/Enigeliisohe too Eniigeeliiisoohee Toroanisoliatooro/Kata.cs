using System.Linq;
using System.Text.RegularExpressions;

public class Main
{
    public static string toexuto(string text)
    {
        var alphabet = string.Concat(Enumerable.Range('a', 26).Select(c => (char) c));
        var vowels = "aeiou";
        var consonants = string.Concat(alphabet.Where(c => !vowels.Contains(c)));
        var patternStart = $@"([{vowels}])(?=[^{vowels}]*";

        return string.Concat(text.Select(c =>
            Regex.IsMatch($"{c}", "[" + consonants + "]", RegexOptions.IgnoreCase)
                ? c + Regex.Match(alphabet, $"{patternStart}{c}).*", RegexOptions.IgnoreCase).Groups[1].Value
                : $"{c}"));
    }
}