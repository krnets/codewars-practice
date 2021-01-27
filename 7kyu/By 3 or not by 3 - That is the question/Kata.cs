using System.Linq;
using System.Numerics;

public static class Kata
{
    static BigInteger[] arr = {3, 6, 9};

    public static bool DivisibleByThree(string n)
    {
        var num = BigInteger.Parse(n);

        return num < 10 ? arr.Contains(num) : DivisibleByThree($"{n.Sum(char.GetNumericValue)}");
    }
}