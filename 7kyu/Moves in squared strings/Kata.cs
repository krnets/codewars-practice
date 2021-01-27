/*using System;
using System.Linq;

public class Opstrings
{
    public static string VertMirror(string strng)
    {
        return string.Join('\n', strng.Split('\n')
            .Select(x => string.Concat(x.Reverse())));
    }

    public static string HorMirror(string strng)
    {
        return string.Concat(VertMirror(strng).Reverse());
    }

    public static string Oper(Func<string, string> fct, string s)
    {
        return fct.Invoke(s);
    }
}*/

using System;
using System.Linq;
using static System.String;

public class Opstrings
{
    public static string VertMirror(string strng)
    {
        return Join('\n', strng.Split('\n').Select(x => Concat(x.Reverse())));
    }

    public static string HorMirror(string strng)
    {
        return Concat(VertMirror(strng).Reverse());
    }

    public static string Oper(Func<string, string> fct, string s)
    {
        return fct(s);
    }
}