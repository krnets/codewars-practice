using System;

class Kata
{
    public static long Layers(long n)
    {
        return (long) (Math.Ceiling((Math.Sqrt(n) + 1) / 2));
    }
}