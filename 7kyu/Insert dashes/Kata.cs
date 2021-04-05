using System.Text.RegularExpressions;

public class Kata
{
    public static string InsertDash(int num)
    {
        return Regex.Replace(num.ToString(), "[13579](?=[13579])", "$0-");
    }
}