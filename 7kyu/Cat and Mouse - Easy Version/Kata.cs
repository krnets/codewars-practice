using System.Text.RegularExpressions;

public class Kata
{
    public static string CatMouse(string x)
    {
        // return Regex.IsMatch(x, "C\\.{4,}m") ? "Escaped!" : "Caught!";
        return Regex.IsMatch(x, @"C.{4,}m") ? "Escaped!" : "Caught!";
    }
}