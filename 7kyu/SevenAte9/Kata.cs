using System.Text.RegularExpressions;

public class Kata
{
    public static string SevenAteNine(string str)
    {
        return Regex.Replace(str, "79(?=7)", "7");
    }
}