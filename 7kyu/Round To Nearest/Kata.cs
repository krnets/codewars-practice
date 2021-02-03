using System;
using System.Linq;

public class Kata
{
    public static int[] RoundUp(int number, int[] list)
    {
        if (list.Length == 0)
            return new int[0];

        int min = list.Min(x => Math.Abs(number - x));

        return list.Where(x => Math.Abs(number - x) == min).ToArray();
    }
}