using System.Text.RegularExpressions;

public class Kata
{
    public static string SplitInParts(string s, int partLength)
    {
        return Regex.Replace(s, "(.{" + partLength + "})(?!$)", "$1 ");
    }
}