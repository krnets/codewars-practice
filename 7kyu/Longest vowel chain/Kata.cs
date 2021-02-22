using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static int Solve(string str)
    {
        return Regex.Split(str, "[^aeiou]+").Max(x => x.Length);
    }
}