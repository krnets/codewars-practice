using System;
using System.Linq;
using System.Text;

public static class Base64Utils
{
    private static readonly string Base64IndexTable;

    static Base64Utils()
    {
        var ABC = Enumerable.Range('A', 26);
        var abc = Enumerable.Range('a', 26);
        var digits = Enumerable.Range('0', 10);
        Base64IndexTable = string.Concat(ABC.Concat(abc).Concat(digits).Select(c => (char) c).Concat("+/"));
    }

    public static string ToBase64(string s)
    {
        if (string.IsNullOrEmpty(s))
            return string.Empty;

        var sb = new StringBuilder();
        var octets = string.Concat(s.Select(c => Convert.ToString(c, 2).PadLeft(8, '0')));

        for (int i = 0; i < octets.Length; i += 6)
        {
            var sextet = octets.Substring(i, Math.Min(6, octets.Length - i)).PadRight(6, '0');
            var fromBinary = Convert.ToInt32(sextet, 2);
            sb.Append(Base64IndexTable[fromBinary]);
        }

        var x = octets.Length / 8 % 3;
        var n = x > 0 ? 3 - x : 0;
        var padding = new string('=', n);

        return sb.Append(padding).ToString();
    }

    public static string FromBase64(string s)
    {
        if (string.IsNullOrEmpty(s))
            return string.Empty;

        var sb = new StringBuilder();
        var n = s.Count(c => c == '=');

        var sextets = string.Concat(s.SkipLast(n)
            .Select(c => Convert.ToString(Base64IndexTable.IndexOf(c), 2).PadLeft(6, '0')));

        for (int i = 0; i < sextets.Length; i += 8)
        {
            var octet = sextets.Substring(i, Math.Min(8, sextets.Length - i));
            var fromBinary = Convert.ToInt32(octet, 2);
            sb.Append((char) fromBinary);
        }

        return sb.ToString().Replace("\0", "");
    }
}