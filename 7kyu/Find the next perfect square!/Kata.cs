using System;

public class Kata
{
    public static long FindNextSquare(long num)
    {
        double next = Math.Sqrt(num) + 1;

        if (next % 1 != 0) return -1;

        return (long) (next * next);
    }
}