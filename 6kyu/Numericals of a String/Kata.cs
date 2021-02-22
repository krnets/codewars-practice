using System.Collections.Generic;
using System.Linq;
using System.Text;

/*
public class JomoPipi
{
    public static string Numericals(string s)
    {
        var sb = new StringBuilder();
        var map = new Dictionary<char, int>();

        foreach (char c in s)
        {
            if (map.ContainsKey(c))
                map[c]++;
            else
                map[c] = 1;

            sb.Append(map[c]);
        }

        return sb.ToString();
    }
}
*/

/*public class JomoPipi
{
    public static string Numericals(string s)
    {
        var sb = new StringBuilder();
        var map = new int[1 << 16];

        foreach (char c in s)
            sb.Append(++map[c]);

        return sb.ToString();
    }
}*/
public class JomoPipi
{
    public static string Numericals(string s)
    {
        var charCount = new int[1 << 16];

        return string.Concat(s.Select(c => ++charCount[c]));
    }
}