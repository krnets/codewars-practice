/*using System;
using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string ParseIPv6(string iPv6)
    {
        return string.Concat(Regex.Split(iPv6, @"[^a-f\d]", RegexOptions.IgnoreCase)
            .Select(block => block.Sum(c => Convert.ToInt32("0x" + c, 16))));
    }
}*/

using System;
using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string ParseIPv6(string iPv6)
    {
        return string.Concat(Regex.Split(iPv6, @"[^0-9A-F]")
            .Select(block => block.Sum(c => Convert.ToInt32(c.ToString(), 16))));
    }
}