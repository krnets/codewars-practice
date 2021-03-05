/*
using System.Numerics;

public class Diagonal
{
    public static BigInteger diagonal(int n, int p)
    {
        BigInteger sum = 1, line = 1, previous = 1;
        var diagonal = new BigInteger(p);
        var end = new BigInteger(n) - diagonal + 1;

        while (line.CompareTo(end) < 0)
        {
            previous = previous * (diagonal + line) / line;
            sum += previous;
            line += BigInteger.One;
        }

        return sum;
    }
}
*/

using System;
using System.Numerics;

public class Diagonal
{
    public static BigInteger diagonal(int n, int p)
    {
        return binomial(n + 1, p + 1);
    }

    private static BigInteger binomial(int n, int k)
    {
        BigInteger product = 1, divisor = 1;

        for (int i = 0; i < Math.Min(k, n - k); i++)
        {
            product *= n - i;
            divisor *= i + 1;
        }

        return product / divisor;
    }
}