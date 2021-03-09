using System;

public static class Kata
{
    public static string ZeroFill(int number, int size)
    {
        return Math.Abs(number).ToString().PadLeft(size, '0');
    }
}