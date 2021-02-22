/*using System.Linq;

public class Kata
{
    public static string SortTheInnerContent(string words)
    {
        return string.Join(" ", words.Split(" ")
            .Select(w =>
                // w.Length < 2 ? w : $"{w[0]}" + $"{string.Concat(w[1..^1].OrderByDescending(c => c))}" + $"{w[^1]}"));
                // w.Length < 2 ? w : w.First() + $"{string.Concat(w[1..^1].OrderByDescending(c => c))}" + w.Last()));
                w.Length < 2
                    ? w
                    : w.First() + string.Concat(w.Skip(1).Take(w.Length - 2).OrderByDescending(c => c)) + w.Last()));
    }
}*/

using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string SortTheInnerContent(string words)
    {
        // return Regex.Replace(words, @"\B\w+\B", m => string.Concat(m.Groups[0].Value.OrderByDescending(c => c)));
        return Regex.Replace(words, @"\B\w+\B", m => string.Concat(m.Value.OrderByDescending(c => c)));
    }
}