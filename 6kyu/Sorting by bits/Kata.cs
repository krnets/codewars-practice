/*using System;
using System.Linq;
using System.Numerics;

public class Kata
{
    public static int[] SortByBit(int[] array)
    {
        var bitCount = array.GroupBy(x => x).ToDictionary(g => g.Key, g => BitOperations.PopCount((uint) g.Key));

        Array.Sort(array, (x, y) => bitCount[x] == bitCount[y] ? x - y : bitCount[x] - bitCount[y]);

        return array;
    }
}*/

using System.Linq;
using System.Numerics;

public class Kata
{
    public static int[] SortByBit(int[] array)
    {
        return array.OrderBy(x => BitOperations.PopCount((uint) x)).ThenBy(x => x).ToArray();
    }
}