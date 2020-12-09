using System.Text.RegularExpressions;

public static class Kata
{
    public static string Disemvowel(string str)
    {
        return Regex.Replace(str, "[aeiou]", "", RegexOptions.IgnoreCase);
    }
}