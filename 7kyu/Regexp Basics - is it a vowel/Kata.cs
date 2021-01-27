using System.Text.RegularExpressions;

public static class Kata
{
    public static bool Vowel(this string s)
    {
        return Regex.IsMatch(s, @"\A[aeiou]\z", RegexOptions.IgnoreCase);
    }
}