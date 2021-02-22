/*using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static string FormatWords(string[] words)
    {
        if (words == null) return string.Empty;

        var str = string.Join(", ", words.Where(w => w.Length > 0));

        // return Regex.Replace(str, @", ([^,]+)$", " and $1");
        return Regex.Replace(str, @", (?=\w+$)", " and ");
    }
}*/

using System.Linq;
using static System.String;
using static System.Text.RegularExpressions.Regex;

public static class Kata
{
    public static string FormatWords(string[] words)
    {
        return words == null
            ? Empty
            : Replace(Join(", ", words.Where(w => !IsNullOrEmpty(w))), @", (?=\w+$)", " and ");
    }
}