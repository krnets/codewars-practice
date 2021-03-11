/*public class Kata
{
    public static string NumberFormat(int number) => $"{number:N0}";
}*/

/*using System.Text.RegularExpressions;

public class Kata
{
    public static string NumberFormat(int number)
    {
        return Regex.Replace(number.ToString(), @"(\d)(?=(\d{3})+\b)", "$1,");
    }
}*/

using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string NumberFormat(int number)
    {
        var matches = Regex.Matches(number.ToString(), @"-?\d{1,3}", RegexOptions.RightToLeft).Select(m => m.Value);

        return string.Join(",", matches.Reverse());
    }
}