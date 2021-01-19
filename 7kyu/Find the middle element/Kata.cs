using System;
using System.Linq;

public class Kata
{
    public static int Gimme(double[] inputArray)
    {
        return Array.IndexOf(inputArray, inputArray.OrderBy(x => x).ToArray()[1]);
    }
}