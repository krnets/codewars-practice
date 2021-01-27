using System;
using System.Linq;

public class Kata
{
    public static Func<int, int[]> MultiplyAll(int[] array) => m => array.Select(n => m * n).ToArray();
}