using System.Linq;

public class SumFractions
{
    public static string SumFracts(int[,] l)
    {
        // if (l.GetLength(0) == 0)
        if (l.Length == 0)
            return null;

        var denom = Enumerable.Range(0, l.GetLength(0))
            .Select(i => l[i, 1])
            .Aggregate(1, (a, b) => a * b);

        var numer = Enumerable.Range(0, l.GetLength(0))
            .Sum(i => l[i, 0] * denom / l[i, 1]);

        var gcd = GCD(numer, denom);

        return gcd == denom ? $"{numer / denom}" : $"[{numer / gcd}, {denom / gcd}]";
    }

    private static int GCD(int a, int b)
    {
        return b == 0 ? a : GCD(b, a % b);
    }
}