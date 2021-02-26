using System;
using System.Linq;

public static class Kata
{
    public static double Chain(double input, Func<double, double>[] fs)
    {
        return fs.Aggregate(input, (current, func) => func(current));
    }
}