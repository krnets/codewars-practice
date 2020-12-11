using System;

public class MinMax
{
    public static int[] minMax(int[] lst)
    {
        int currentMin = Int32.MaxValue;
        int currentMax = Int32.MinValue;

        foreach (int i in lst)
        {
            currentMin = Math.Min(i, currentMin);
            currentMax = Math.Max(i, currentMax);
        }

        return new[] {currentMin, currentMax};
    }
}