using System;
using System.Linq;

public class Kata
{
    public static bool SmallEnough(int[] a, int limit)
    {
        // return a.All(x => x <= limit);
        return Array.TrueForAll(a, x => x <= limit);
    }
}