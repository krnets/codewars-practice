using System;
using System.Linq;

public class Kata
{
    public static int[] Reject(int[] array, Func<int, bool> predicate)
    {
        return array.Where(x => !predicate(x)).ToArray();
    }
}