using System;

public static class Kata
{
    public static int MaxSequence(int[] arr)
    {
        int curMax = 0, resMax = 0;

        foreach (int x in arr)
        {
            curMax = Math.Max(0, curMax + x);
            resMax = Math.Max(resMax, curMax);
        }

        return resMax;
    }
}