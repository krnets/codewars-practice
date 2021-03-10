using System.Linq;
using System.Text.RegularExpressions;

public class Decoding
{
    public static string Decode(string r)
    {
        var num = int.Parse(Regex.Match(r, "\\d+").Value);
        var code = Regex.Match(r, "\\D+").Value;

        var plain = code.Select(c => Enumerable.Range(0, 26).FirstOrDefault(i => c - 'a' == i))
            .SelectMany(y => Enumerable.Range(0, 26)
                .Where(x => x * num % 26 == y))
            .Select(i => (char) ('a' + i)).ToArray();

        return code.Length == plain.Length ? string.Concat(plain) : "Impossible to decode";
    }
}