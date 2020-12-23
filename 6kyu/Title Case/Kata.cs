using System.Linq;
using static System.Char;
using static System.String;

public class Kata
{
    public static string TitleCase(string title, string minorWords = "")
    {
        return IsNullOrEmpty(title)
            ? Empty
            : Join(" ",
                title.ToLower().Split().Select((s, i) => IsNullOrEmpty(minorWords)
                    ? ToUpper(s[0]) + s[1..]
                    : minorWords.ToLower().Split().Contains(s) && i != 0
                        ? s
                        : ToUpper(s[0]) + s[1..]).ToArray());
    }
}