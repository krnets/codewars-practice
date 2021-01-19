/*using System;
using System.Linq;

public static class Kata
{
    public static bool PowerOfTwo(int n)
    {
        return Convert.ToString(n, 2).Count(x => x == '1') == 1;
    }
}*/

/*using System.Numerics;

public static class Kata
{
    public static bool PowerOfTwo(int n)
    {
        return new BigInteger(n).IsPowerOfTwo;
    }
}*/

/*using System;

public static class Kata
{
    public static bool PowerOfTwo(int n)
    {
        return Math.Log2(n) % 1 == 0;
    }
}*/
public static class Kata
{
    public static bool PowerOfTwo(int n)
    {
        int m = 1;

        while (m <= n)
        {
            if (m == n) return true;
            m <<= 1;
        }
        return false;
    }
}