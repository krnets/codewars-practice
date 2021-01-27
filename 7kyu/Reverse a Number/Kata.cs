/*public class Kata
{
    public int ReverseNumber(int n)
    {
        int reversed = 0;

        while (n != 0)
        {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }

        return reversed;
    }
}*/

using System;
using System.Linq;

public class Kata
{
    public int ReverseNumber(int n)
    {
        return Math.Sign(n) * int.Parse(string.Concat($"{Math.Abs(n)}".Reverse()));
    }
}