using System.Text.RegularExpressions;

public static class Kata
{
    public static string StringBreakers(int n, string str)
    {
        return string.Join("\n", Regex.Split(str.Replace(" ", ""), @"(?<=\G.{" + n + "})")).TrimEnd();
    }
}

/*using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static string StringBreakers(int n, string str)
    {
        return string.Join("\n", Regex.Matches(str.Replace(" ", ""), $@"\w{{1,{n}}}").Select(m => m.Value));
    }
}*/

/*public static class Kata
{
    public static string StringBreakers(int n, string str)
    {
        var sb = new StringBuilder();
        var i = n;

        foreach (var c in str.Where(c => c != ' '))
        {
            if (i == 0)
            {
                sb.Append('\n');
                i = n;
            }

            sb.Append(c);
            i--;
        }

        return sb.ToString();
    }
}*/