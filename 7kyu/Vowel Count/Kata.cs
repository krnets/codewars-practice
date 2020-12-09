using System.Linq;

public static class Kata
{
    private const string Vowels = "aeiou";

    public static int GetVowelCount(string str) => str.Count(c => Vowels.Contains(c));
}