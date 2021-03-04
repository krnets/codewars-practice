using System;
using System.Linq;

public class Opstrings
{
    public static string Rot90Counter(string strng)
    {
        var matrix = strng.Split("\n").Select(row => row.Reverse().ToArray()).ToArray();

        for (int i = 0; i < matrix.Length; i++)
            for (int j = i; j < matrix.Length; j++)
                (matrix[i][j], matrix[j][i]) = (matrix[j][i], matrix[i][j]);

        return string.Join("\n", matrix.Select(row => string.Concat(row)));
    }

    public static string Diag2Sym(string strng)
    {
        return string.Join("\n", Rot90Counter(strng).Split("\n").Select(row => string.Concat(row.Reverse())));
    }

    public static string SelfieDiag2Counterclock(string strng)
    {
        var original = strng.Split("\n");
        var transposedOpposite = Diag2Sym(strng).Split("\n");
        var rotateLeftReversed = Rot90Counter(strng).Split("\n");

        return string.Join("\n", Enumerable.Range(0, original.Length)
            .Select(i => $"{original[i]}|{transposedOpposite[i]}|{rotateLeftReversed[i]}"));
    }

    public static string Oper(Func<string, string> fct, string s)
    {
        return fct(s);
    }
}