using System;
using System.Linq;

public class Predicter
{
    public static int PredictAge(params int[] ages)
    {
        return (int)(Math.Sqrt(ages.Sum(x => x * x)) / 2);
    }
}