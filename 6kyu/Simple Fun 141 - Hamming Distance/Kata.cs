/*using System;
using System.Linq;

public class Kata
{
    public int HammingDistance(int a, int b)
    {
        var aBinary = Convert.ToString(a, 2).PadLeft(20, '0');
        var bBinary = Convert.ToString(b, 2).PadLeft(20, '0');

        return aBinary.Zip(bBinary, (f, s) => f != s).Count(x => x);
    }
}*/

/*public class Kata
{
    public int HammingDistance(int a, int b) => HammingDistance(a ^ b);

    public int HammingDistance(int n) => n == 0 ? 0 : 1 + HammingDistance(n & (n - 1));
}*/

public class Kata
{
    public int HammingDistance(int a, int b)
    {
        int count = 0;
        int x = a ^ b;

        while (x != 0)
        {
            count += x & 1;
            x >>= 1;
        }

        return count;
    }
}