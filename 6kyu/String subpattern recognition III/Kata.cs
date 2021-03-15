using System.Linq;

class Kata
{
    public static string HasSubpattern(string str)
    {
        var charCount = str.GroupBy(c => c).ToDictionary(g => g.Key, g => g.Count());
        int m = charCount.Values.Aggregate(Gcd);

        // return string.Concat(charCount.SelectMany(p => new string(p.Key, p.Value / m)).OrderBy(c => c));
        return string.Concat(charCount.OrderBy(p => p.Key).Select(p => new string(p.Key, p.Value / m)));
    }

    private static int Gcd(int a, int b) => b == 0 ? a : Gcd(b, a % b);
}