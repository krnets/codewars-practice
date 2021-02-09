/*using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static string GroupByCommas(int n)
    {
        return string.Join(",", Regex.Split(n.ToString(), @"(?=(?:\d{3})+$)").Where(x => x.Length > 0));
    }
}*/

public static class Kata
{
    public static string GroupByCommas(int n) => $"{n:N0}";
}