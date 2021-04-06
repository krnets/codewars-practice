using System.Text.RegularExpressions;

public class Kata
{
    public static bool Alphanumeric(string str)
    {
        return Regex.IsMatch(str, @"^[A-Za-z\d]+$");
    }
}