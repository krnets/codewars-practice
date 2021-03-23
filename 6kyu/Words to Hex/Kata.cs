using System.Linq;

public class Kata
{
    public static string[] WordsToHex(string words)
    {
        return words.Split(" ")
            .Select(w => '#' + string.Concat(w.Take(3).Select(c => $"{(int) c:x}")).PadRight(6, '0'))
            .ToArray();
    }
}