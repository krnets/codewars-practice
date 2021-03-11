using System.Numerics;

class Cycle
{
    public static int Running(int n)
    {
        if (n % 2 == 0 || n % 5 == 0) return -1;
        int exponent = 1;

        while (BigInteger.ModPow(10, exponent, n) != 1)
            exponent++;
        
        return exponent;
    }
}