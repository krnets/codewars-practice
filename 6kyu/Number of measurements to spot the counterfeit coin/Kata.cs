using System;

class Kata
{
    public static long HowManyMeasurements(long n)
    {
        return (long) Math.Ceiling(Math.Log(n, 3));
    }
}