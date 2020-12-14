/*
using System;
using System.Linq;

public class Kata
{
    public static int CountBits(int n)
    {
        return Convert.ToString(n, 2).Count(c => c == '1');
    }
}
*/

/*public class Kata
{
    public static int CountBits(int n)
    {
        int count = 0;

        while (n > 0)
        {
            count += n & 1;
            n >>= 1;
        }

        return count;
    }
}*/

/*
public class Kata
{
    public static int CountBits(int n)
    {
        return n == 0 ? 0 : (n & 1) + CountBits(n >> 1);
    }
}
*/

using System.Numerics;

public class Kata
{
    public static int CountBits(int n)
    {
        return BitOperations.PopCount((uint) n);
    }
}