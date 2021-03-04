using System;
using System.Linq;

public class Opstrings
{
    public static string Rot90Clock(string strng)
    {
        return string.Join("\n", Diag1Sym(strng).Split("\n").Select(sub => string.Concat(sub.Reverse())));
    }

    public static string Diag1Sym(string strng)
    {
        var matrix = strng.Split("\n").Select(row => row.ToCharArray()).ToArray();

        for (int i = 0; i < matrix.Length; i++)
            for (int j = i; j < matrix.Length; j++)
                (matrix[i][j], matrix[j][i]) = (matrix[j][i], matrix[i][j]);

        return string.Join("\n", matrix.Select(row => string.Concat(row)));
    }

    public static string SelfieAndDiag1(string strng)
    {
        var original = strng.Split("\n");
        var transposed = Diag1Sym(strng).Split("\n");

        return string.Join("\n", original.Zip(transposed, (a, b) => $"{a}|{b}"));
    }

    public static string Oper(Func<string, string> fct, string s)
    {
        return fct(s);
    }
}
