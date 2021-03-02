using System.Text.RegularExpressions;

public static class Kata
{
    public static string RemoveParentheses(string s)
    {
        var pattern = @"\([^()]*\)";

        while (Regex.IsMatch(s, pattern))
            s = Regex.Replace(s, pattern, "");

        return s;
    }
}

/*
using System.Text.RegularExpressions;

public static class Kata
{
    private const string pattern = @"\([^()]*\)";

    public static string RemoveParentheses(string s)
    {
        return Regex.IsMatch(s, pattern) ? RemoveParentheses(Regex.Replace(s, pattern, "")) : s;
    }
}
*/