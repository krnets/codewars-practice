using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static int Solve(string s)
    {
        // return Regex.Split(s, "\\D+").Where(x => x.Length > 0).Max(int.Parse);
        return Regex.Matches(s, "\\d+").Max(x => int.Parse(x.Value));
    }
}