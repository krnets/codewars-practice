using System.Linq;

public class Updown
{
    public static string Arrange(string strng)
    {
        var words = strng.Split(" ");

        for (int i = 0; i < words.Length - 1; i++)
            if (words[i + i % 2].Length > words[i + 1 - i % 2].Length)
                (words[i], words[i + 1]) = (words[i + 1], words[i]);

        return string.Join(" ", words.Select((w, i) => i % 2 == 0 ? w.ToLower() : w.ToUpper()));
    }
}