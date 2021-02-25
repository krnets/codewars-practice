using System;

public class Numbers
{
    public static double TwoDecimalPlaces(double number)
    {
        // return (double) ((int) (number * 100)) / 100;
        // return (long) (number * 100) / 100d;
        return Math.Truncate(number * 100) / 100;
    }
}