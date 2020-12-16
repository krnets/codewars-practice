using System.Collections.Generic;
using System.Text;

public class Kata
{
    public static string DuplicateEncode(string word)
    {
        var map = new Dictionary<char, int>();
        var chars = word.ToLower().ToCharArray();

        foreach (char c in chars)
            if (map.ContainsKey(c))
                map[c]++;
            else map[c] = 1;

        var sb = new StringBuilder();

        foreach (char c in chars)
            sb.Append(map[c] > 1 ? ')' : '(');

        return sb.ToString();
    }
}