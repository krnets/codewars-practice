using System.Linq;

public static class Kata
{
    public static string Dative(string word)
    {
        var frontVowel = "eéiíöőüű";
        var backVowel = "aáoóuú";

        foreach (char c in word.Reverse())
        {
            if (frontVowel.Contains(c)) return word + "nek";
            if (backVowel.Contains(c)) return word + "nak";
        }

        return word;
    }
}