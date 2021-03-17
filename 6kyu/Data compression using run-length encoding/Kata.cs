/*using System.Linq;
using System.Text.RegularExpressions;


public class RleCompression
{
    public string Encode(string input)
    {
        return string.Concat(Regex.Matches(input, @"((.)\2*)")
            .Select(m => $"{m.Length}{m.Value[0]}"));
    }

    public string Decode(string input)
    {
        return string.Concat(Regex.Matches(input, @"((\d+)(\w))")
            .Select(m => new string(m.Groups[3].Value[0], int.Parse(m.Groups[2].Value))));
    }
}*/

/*using System.Text.RegularExpressions;


public class RleCompression
{
    public string Encode(string input)
    {
        return Regex.Replace(input, @"((.)\2*)", m => $"{m.Length}{m.Value[0]}");
    }

    public string Decode(string input)
    {
        return Regex.Replace(input, @"((\d+)(\w))", m => new string(m.Groups[3].Value[0], int.Parse(m.Groups[2].Value)));
    }
}*/

using System;
using System.Text.RegularExpressions;


public class RleCompression
{
    public string Encode(string input)
    {
        return Regex.Replace(input, @"(\w)\1*", m => $"{m.Length}{m.Value[0]}");
    }

    public string Decode(string input)
    {
        return Regex.Replace(input, @"((?<count>\d+)(?<char>\w))", m => new string(Convert.ToChar(m.Groups["char"].Value), int.Parse(m.Groups["count"].Value)));
    }
}