/*
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

public class CodeDecode
{
    private static List<string> digitCode = new List<string>
        {"10", "11", "0110", "0111", "001100", "001101", "001110", "001111", "00011000", "00011001"};

    public static string Code(string strng) =>
        string.Concat(strng.Select(c => digitCode[(int) char.GetNumericValue(c)]));

    public static string Decode(string str) =>
        Regex.Replace(str, string.Join("|", digitCode), m => $"{digitCode.IndexOf(m.Value)}");
}
*/

/*using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

public class CodeDecode
{
    private static List<string> digitCode = Enumerable.Range(0, 10)
        .Select(i => "1".PadLeft(i < 4 ? i & 2 : i < 8 ? 3 : 4, '0') + Convert.ToString(i, 2)).ToList();

    public static string Code(string strng) =>
        string.Concat(strng.Select(c => digitCode[c - '0']));

    public static string Decode(string str) =>
        Regex.Replace(str, string.Join("|", digitCode), m => $"{digitCode.IndexOf(m.Value)}");
}*/

using System;
using System.Linq;

public class CodeDecode
{
    public static string Code(string strng) =>
        string.Concat(strng
            .Select(c => Convert.ToString(c - '0', 2))
            .Select(b => "1".PadLeft(b.Length, '0') + b));

    public static string Decode(string str)
    {
        int i = str.IndexOf('1') + 1;

        return i == 0
            ? string.Empty
            : Convert.ToInt32(str.Substring(i, i), 2) + Decode(str.Substring(i + i));
    }
}