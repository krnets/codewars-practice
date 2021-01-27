using System;
using System.Linq;

public class Kata
{
    public static int FindSmallest(int[] numbers, string toReturn)
    {
        return toReturn switch
        {
            "value" => numbers.Min(),
            "index" => Array.IndexOf(numbers, numbers.Min()),
            _ => throw new ArgumentException()
        };
    }
}