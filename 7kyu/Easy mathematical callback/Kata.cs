using System;
using System.Linq;

public class Kata
{
    public static int[] ProcessArray(int[] arr, Func<int, int> callback)
    {
        return arr.Select(callback).ToArray();
    }
}