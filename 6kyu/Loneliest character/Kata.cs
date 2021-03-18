/*using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static char[] Loneliest(string result)
    {
        var seq = Regex.Matches(result.Trim(), @"(?=(?<slices>\s*\w\s*))").Select(m => m.Groups["slices"].Value);
        var max = seq.Max(s => s.Length);

        return seq.Where(s => s.Length == max).Select(s => char.Parse(s.Trim())).ToArray();
    }
}*/

using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static char[] Loneliest(string result)
    {
        var seq = Regex.Matches(result.Trim(), @"(?<!\s)(?=(?<slices>\s*\w\s*))").Select(m => m.Groups["slices"].Value);
        var max = seq.Max(s => s.Length);

        return seq.Where(s => s.Length == max).Select(s => char.Parse(s.Trim())).ToArray();
    }
}