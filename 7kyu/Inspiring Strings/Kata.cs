using System.Linq;

public class Kata
{
    public static string LongestWord(string stringOfWords)
    {
        return stringOfWords.Split(" ").OrderBy(x => x.Length).Last();
    }
}