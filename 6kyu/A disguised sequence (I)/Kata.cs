/*using System.Numerics;

public class HiddenSeq
{
    public static BigInteger fcn(int n)
    {
        // return BigInteger.Pow(2, n);
        return BigInteger.One << n;
    }
}*/

using System.Numerics;

public class HiddenSeq
{
    public static BigInteger fcn(int n) => BigInteger.One << n;
}