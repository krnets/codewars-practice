public static class Kata
{
    public static bool IsNegativeZero(double n)
    {
        // return double.IsNegative(n) && n == 0;
        return double.IsNegativeInfinity(1 / n);
    }
}

/*using System;

public static class Kata
{
    public static bool IsNegativeZero(double n)
    {
        return BitConverter.DoubleToInt64Bits(n) == BitConverter.DoubleToInt64Bits(-0.0);
    }
}*/