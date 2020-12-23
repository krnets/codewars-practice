/*using System.Collections.Generic;
using System.Text;

public class Kata
{
    public static string ToWeirdCase(string s)
    {
        var list = new List<string>();

        foreach (var word in s.Split())
        {
            var sb = new StringBuilder();

            for (int i = 0; i < word.Length; i++)
                sb.Append(i % 2 == 0 ? char.ToUpper(word[i]) : char.ToLower(word[i]));

            list.Add(sb.ToString());
        }

        return string.Join(" ", list);
    }
}*/

using System.Linq;

public class Kata
{
    public static string ToWeirdCase(string s)
    {
        return string.Join(" ",
            s.Split().Select(word => string.Concat(
                word.Select((c, i) => i % 2 == 0 ? char.ToUpper(c) : char.ToLower(c)))));
    }
}