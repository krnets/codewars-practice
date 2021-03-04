using System;
using System.Linq;

public class Solution
{
    public static int solve(int[] arr)
    {
        return Math.Min(arr.Sum() / 2, arr.Sum() - arr.Max());
    }
}