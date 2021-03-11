using System;

public class Kata
{
    public static void WaveSort(int[] arr)
    {
        Array.Sort(arr);

        for (int i = 0; i < arr.Length - 1; i += 2)
            (arr[i], arr[i + 1]) = (arr[i + 1], arr[i]);
    }
}