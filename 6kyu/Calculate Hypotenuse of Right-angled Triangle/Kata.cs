using System;

public class Kata
{
    public static double CalculateHypotenuse(double a, double b)
    {
        return a > 0 && b > 0 ? Math.Round(Math.Sqrt(a * a + b * b), 3) : throw new ArgumentException();
    }
}