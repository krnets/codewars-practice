/*using System.Numerics;

class QuickCalc
{
    public static BigInteger Choose(int n, int p)
    {
        var ans = BigInteger.One;

        for (int i = 0; i < p; i++)
            ans = BigInteger.Divide(BigInteger.Multiply(ans, n - i), i + 1);

        return ans;
    }
}*/

using System.Numerics;

class QuickCalc
{
    public static BigInteger Choose(int n, int k)
    {
        return k == 0 ? 1 : Choose(n - 1, k - 1) * n / k;
    }
}