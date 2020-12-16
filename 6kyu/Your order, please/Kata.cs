/*using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static string Order(string words)
    {
        return !words.Any()
            ? words
            : string.Join(' ', words.Split(' ').OrderBy(w => int.Parse(Regex.Match(w, @"\d+").Value)));
    }
}*/

using System.Linq;

public static class Kata
{
    public static string Order(string words)
    {
        return string.Join(" ", words.Split().OrderBy(w => w.SingleOrDefault(char.IsDigit)));
    }
}