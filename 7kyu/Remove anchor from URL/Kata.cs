using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static string RemoveUrlAnchor(string url)
    {
        return Regex.Matches(url, "^[^#]*").First().ToString();
    }
}