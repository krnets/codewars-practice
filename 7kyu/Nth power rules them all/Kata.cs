using System;
using System.Linq;

public class Kata
{
    public static int ModifiedSum(int[] a, int n)
    {
        // return (int) (a.Sum(x => Math.Pow(x, n)) - a.Sum());
        return (int) a.Sum(x => Math.Pow(x, n) - x);
    }
}