/*using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string SmallWordHelper(string sentence)
    {
        return string.Join(' ', sentence.Split(' ')
            .Select(w => w.Length <= 3
                ? w.ToUpper()
                : string.Concat(
                    w.Where(c => !Regex.IsMatch(c.ToString(), "[aeiou]", RegexOptions.IgnoreCase)))));
    }
}*/

using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string SmallWordHelper(string sentence)
    {
        const string vowels = @"[aeiou]";

        return string.Join(" ", sentence.Split(" ")
            .Select(word => word.Length <= 3
                ? word.ToUpper()
                : Regex.Replace(word, vowels, string.Empty, RegexOptions.IgnoreCase)));
    }
}