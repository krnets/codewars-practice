using System.Linq;

public static class Kata
{
    public static string AlphabetPosition(string text)
    {
        var letterPos = text.ToLower()
            .Where(char.IsLetter)
            .Select(c => c - 'a' + 1);

        return string.Join(' ', letterPos);
    }
}