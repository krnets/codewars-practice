using System;
using System.Globalization;

public static class Kata
{
    public static double CalculateAreaOfCircle(string radius)
    {
        double r;
        var style = NumberStyles.AllowDecimalPoint;
        var culture = CultureInfo.CreateSpecificCulture("en-AU");

        if (!double.TryParse(radius, style, culture, out r) || r < 1)
            throw new ArgumentException();

        return Math.Round(Math.PI * r * r, 2);
    }
}