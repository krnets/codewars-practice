using System.Text.RegularExpressions;

public class Kata
{
    public static int FilterString(string s)
    {
        return int.Parse(Regex.Replace(s, "\\D", ""));
    }
}