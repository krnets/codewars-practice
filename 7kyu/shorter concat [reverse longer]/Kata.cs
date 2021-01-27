using System.Linq;

class ReverseLonger
{
    public static string ShorterReverseLonger(string a, string b)
    {
        a ??= string.Empty;
        b ??= string.Empty;

        if (a.Length < b.Length)
            (a, b) = (b, a);

        return b + string.Concat(a.Reverse()) + b;
    }
}