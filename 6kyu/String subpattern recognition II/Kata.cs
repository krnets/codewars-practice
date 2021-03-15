using System.Linq;

class Kata
{
    public static bool HasSubpattern(string str) => str.GroupBy(c => c).Select(g => g.Count()).Aggregate(Gcd) > 1;

    private static int Gcd(int a, int b) => b == 0 ? a : Gcd(b, a % b);
}