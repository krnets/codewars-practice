/*using System.Numerics;

public class SumFct
{
    public static BigInteger perimeter(BigInteger n)
    {
        BigInteger a = 1, b = 1, sum = 0;

        for (BigInteger i = 0; i <= n; i++)
        {
            sum += a;
            (a, b) = (b, a + b);
        }

        return BigInteger.Multiply(4, sum);
    }
}*/

using System.Numerics;

public class SumFct
{
    public static BigInteger perimeter(BigInteger n)
    {
        BigInteger a = 1, b = 1, sum = 0;

        while (n >= 0)
        {
            sum += a;
            (a, b) = (b, a + b);
            n--;
        }

        return BigInteger.Multiply(4, sum);
    }
}