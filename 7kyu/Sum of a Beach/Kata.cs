using System.Text.RegularExpressions;

public class Kata
{
    public static int SumOfABeach(string s)
    {
        return Regex.Matches(s, "Sand|Water|Fish|Sun", RegexOptions.IgnoreCase).Count;
    }
}