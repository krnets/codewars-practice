using System;

public static class Kata
{
    public static int Solution(int[] items, int index, int defaultValue)
    {
        // return Math.Abs(index) <= items.Length ? items[index < 0 ? items.Length + index : index] : defaultValue;
        // return items.Length < Math.Abs(index) ? defaultValue : items[index < 0 ? items.Length + index : index];
        return Math.Abs(index) > items.Length ? defaultValue : items[index < 0 ? items.Length + index : index];
    }
}