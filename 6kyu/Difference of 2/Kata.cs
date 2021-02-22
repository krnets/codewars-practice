/*using System;
using System.Linq;

public class Kata
{
    public static (int, int)[] TwosDifference(int[] array)
    {
        return array.Where(x => Array.IndexOf(array, x + 2) != -1)
            .Select(x => (x, x + 2))
            .Distinct()
            .OrderBy(x => x)
            .ToArray();
    }
}*/

using System;
using System.Linq;

public class Kata
{
    public static (int, int)[] TwosDifference(int[] array)
    {
        return array.OrderBy(x => x)
            .Select(x => (x, x + 2))
            .Where(tuple => Array.Exists(array, y => tuple.Item2 == y))
            .ToArray();
    }
}