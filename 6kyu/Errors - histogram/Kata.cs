/*using System.Linq;
using System.Text.RegularExpressions;

public class Hist
{
    public static string hist(string s)
    {
        var list = (from errorChar in "uwxz"
            where s.Contains(errorChar)
            let count = Regex.Replace(s, "[^" + errorChar + "]", "").Length
            select $"{errorChar}  {count}{new string(' ', 6 - $"{count}".Length)}{new string('*', count)}").ToList();

        return string.Join("\r", list);
    }
}*/

using System.Linq;
using System.Text.RegularExpressions;

public class Hist
{
    public static string hist(string s)
    {
        return string.Join("\r", (from errorChar in "uwxz"
            where s.Contains(errorChar)
            let count = Regex.Replace(s, "[^" + errorChar + "]", "").Length
            select $"{errorChar}  {count}{"".PadLeft(6 - $"{count}".Length)}{new string('*', count)}"));
    }
}