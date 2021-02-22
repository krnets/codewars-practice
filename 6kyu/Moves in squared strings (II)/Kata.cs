using System;
using System.Linq;

public class Opstrings1
{
    public static string Oper(Func<string, string> fct, string s) => fct.Invoke(s);

    public static string Rot(string strng) => string.Concat(strng.Reverse());

    public static string SelfieAndRot(string strng)
    {
        var withDots = string.Join("\n", strng.Split("\n")
            .Select(sub => sub + new string('.', sub.Length)));

        return string.Join("\n", withDots, Rot(withDots));
    }
}