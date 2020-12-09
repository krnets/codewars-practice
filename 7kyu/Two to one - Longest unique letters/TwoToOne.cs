using System.Linq;

public class TwoToOne
{
    public static string Longest(string s1, string s2)
    {
        // return string.Concat(s1.Union(s2).OrderBy(c => c));
        // return string.Concat((s1 + s2).Distinct().OrderBy(c => c));
        return new string((s1 + s2).Distinct().OrderBy(c => c).ToArray());
    }
}