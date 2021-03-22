/*using System;
using System.Linq;

public class Kata
{
    public static int NormIndex(int[] array, int index)
    {
        return index < 0
            ? array.Reverse().ElementAt(Math.Abs(index + 1) % array.Length)
            : array[index % array.Length];
    }
}*/

public class Kata
{
    public static int NormIndex(int[] array, int index)
    {
        var i = (index % array.Length + array.Length) % array.Length;

        return array[i];
    }
}