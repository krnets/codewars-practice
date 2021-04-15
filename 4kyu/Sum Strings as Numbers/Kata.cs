using System.Numerics;

public static class Kata
{
    public static string sumStrings(string a, string b)
    {
        var bigA = BigInteger.Parse(string.IsNullOrEmpty(a) ? "0" : a);
        var bigB = BigInteger.Parse(string.IsNullOrEmpty(b) ? "0" : b);

        return BigInteger.Add(bigA, bigB).ToString();
    }
}