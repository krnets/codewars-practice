using System;
using System.Linq;

public class Kata
{
    public static bool One(int[] arr, Func<int, bool> fun)
    {
        // return arr.Where(fun).Count() == 1;
        return arr.Count(fun) == 1;
    }
}