/*public class Kata
{
    public static int? FoldTo(double distance)
    {
        if (distance < 0)
            return null;

        double thickness = 0.0001;
        int folds = 0;

        while (thickness < distance)
        {
            thickness *= 2;
            folds++;
        }

        return folds;
    }
}*/

using System;

public class Kata
{
    private const double Thickness = 0.0001;

    public static int? FoldTo(double distance)
    {
        return (distance < 0) ? null :
               (distance < Thickness) ? 0 :
               (int?) Math.Ceiling(Math.Log(distance / Thickness, 2));
    }
}