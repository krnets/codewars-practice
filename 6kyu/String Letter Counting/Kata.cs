using System.Linq;

public class Kata
{
    public static string StringLetterCount(string str)
    {
        return string.Concat(str.ToLower()
            .Where(char.IsLetter)
            .GroupBy(c => c)
            .OrderBy(g => g.Key)
            .Select(g => $"{g.Count()}{g.Key}"));
    }
}