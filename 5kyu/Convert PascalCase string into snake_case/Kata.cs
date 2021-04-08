/*using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static string ToUnderscore(int str)
    {
        return str.ToString();
    }

    public static string ToUnderscore(string str)
    {
        return string.Join("_", Regex.Matches(str, @"([A-Z])([a-z\d])*").Select(m => m.Groups[0].Value.ToLower()));
    }
}*/

using System.Text.RegularExpressions;

public static class Kata
{
    public static string ToUnderscore(int str)
    {
        return str.ToString();
    }

    public static string ToUnderscore(string str)
    {
        return Regex.Replace(str, @"(.)([A-Z])", @"$1_$2").ToLower();
    }
}