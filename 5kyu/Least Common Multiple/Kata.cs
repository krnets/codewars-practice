using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static int Lcm(List<int> nums)
    {
        return nums.Aggregate(1, (a, b) => a * b / Gcd(a, b));
    }

    private static int Gcd(int a, int b)
    {
        return b == 0 ? a : Gcd(b, a % b);
    }
}