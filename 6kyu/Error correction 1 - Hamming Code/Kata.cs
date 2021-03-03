/*using System;
using System.Linq;
using System.Text.RegularExpressions;

public class CodeWars
{
    public static string encode(string text)
    {
        return string.Concat(text.Select(c => string.Concat(
            Convert.ToString(c, 2).PadLeft(8, '0')
                .Select(bit => new string(bit, 3)))));
    }

    public static string decode(string bits)
    {
        var corrected = string.Concat(Regex.Split(bits, @"(\d{3})")
            .Where(x => x.Length > 0)
            .Select(x => x.Sum(char.GetNumericValue) > 1 ? '1' : '0'));

        // var corrected = string.Concat(Enumerable.Range(0, bits.Length / 3)
        //     .Select(i => bits.Substring(i * 3, 3))
        //     .Select(x => x.Sum(char.GetNumericValue) > 1 ? '1' : '0'));

        return string.Concat(Enumerable.Range(0, corrected.Length / 8)
            .Select(i => (char) Convert.ToInt32(corrected.Substring(i * 8, 8), 2)));
    }
}*/

using System;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

public class CodeWars
{
    public static string encode(string text)
    {
        return string.Concat(Encoding.ASCII.GetBytes(text)
            .SelectMany(b => Convert.ToString(b, 2).PadLeft(8, '0')
                .Select(c => new string(c, 3))));
    }

    public static string decode(string bits)
    {
        var binary = string.Concat(Regex.Split(bits, @"(?<=\G.{3})")
            .Select(s => s.Sum(char.GetNumericValue) > 1 ? '1' : '0'));

        return Encoding.ASCII.GetString(Enumerable.Range(0, binary.Length / 8)
            .Select(i => Convert.ToByte(binary.Substring(i * 8, 8), 2)).ToArray());
    }
}