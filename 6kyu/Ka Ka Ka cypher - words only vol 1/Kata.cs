using System.Text.RegularExpressions;

public class Kata
{
    public static string KaCokadekaMe(string word)
    {
        return "ka" + Regex.Replace(word, @"([aeiou])([^aeiou])", "$1ka$2", RegexOptions.IgnoreCase);
    }
}