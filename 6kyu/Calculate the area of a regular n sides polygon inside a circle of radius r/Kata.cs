using System;

public class Calculator
{
    public static double AreaOfPolygonInsideCircle(double circleRadius, int numberOfSides)
    {
        var turn = 2 * Math.PI;
        var area = 1.0 / 2 * numberOfSides * Math.Pow(circleRadius, 2) * Math.Sin(turn / numberOfSides);

        return Math.Round(area, 3);
    }
}