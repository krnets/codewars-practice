/*public class Kata
{
    public static bool IsAlt(string word)
    {
        var vowels = "aeiou";
        var isVowel = vowels.Contains(word[0]);

        for (int i = 1; i < word.Length; i++)
        {
            if (vowels.Contains(word[i..(i + 1)]) == isVowel)
                return false;

            isVowel = !isVowel;
        }

        return true;
    }
}*/

using System.Text.RegularExpressions;

public class Kata
{
    public static bool IsAlt(string word)
    {
        return !Regex.IsMatch(word, "[aeiou]{2}|[^aeiou]{2}");
    }
}