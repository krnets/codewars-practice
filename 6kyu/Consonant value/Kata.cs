using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static int Solve(string s)
    {
        return Regex.Split(s, "[aeiou]+").Max(sub => sub.Sum(c => c - 'a' + 1));
    }
}

/*using System;
using System.Linq;

public class Kata
{
    public static int Solve(string s)
    {
        return s.Split("aeiou".ToCharArray(), StringSplitOptions.RemoveEmptyEntries)
            .Max(str => str.Sum(c => c - 'a' + 1));
    }
}*/