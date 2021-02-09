using System.Text.RegularExpressions;

public class Abbreviator
{
    public static string Abbreviate(string input)
    {
        return Regex.Replace(input, @"\B\w{2,}\B", m => $"{m.Length}");
    }
}