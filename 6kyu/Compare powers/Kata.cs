using System;

class Kata
{
    public static int ComparePowers(int[] a, int[] b)
    {
        var x = Math.Pow(a[0], a[1]);
        var y = Math.Pow(b[0], b[1]);

        return x < y ? 1 : x > y ? -1 : 0;
    }
}