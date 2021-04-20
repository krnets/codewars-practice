using System.Linq;

public class Kata
{
    public static bool ValidateString(string[] dictionary, string word)
    {
        word = dictionary.Reverse().Aggregate(word, (current, w) => current.Replace(w, ""));

        return string.IsNullOrEmpty(word);
    }
}