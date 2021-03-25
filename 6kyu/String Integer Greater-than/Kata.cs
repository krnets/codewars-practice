using System.Numerics;

public class Kata
{
    public static bool StringIntGreaterThan(string a, string b)
    {
        return BigInteger.Parse(a).CompareTo(BigInteger.Parse(b)) > 0;
    }
}