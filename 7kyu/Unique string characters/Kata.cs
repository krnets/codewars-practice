using System.Linq;

public static class Kata
{
    public static string Solve(string a, string b)
    {
        return string.Concat((a + b).Where(c => a.Contains(c) ^ b.Contains(c)));
    }
}

/*using System.Text.RegularExpressions;

public static class Kata
{
    public static string Solve(string a, string b)
    {
        return Regex.Replace(a, $"[{b}]", "") + Regex.Replace(b, $"[{a}]", "");
    }
}*/

/*using System.Linq;

public static class Kata
{
    public static string Solve(string a, string b)
    {
        var set = a.Intersect(b).ToHashSet();

        return string.Concat((a + b).Where(c => !set.Contains(c)));
    }
}*/