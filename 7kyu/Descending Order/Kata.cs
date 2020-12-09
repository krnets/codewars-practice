/*
using System;
using System.Linq;

public static class Kata
{
    public static int DescendingOrder(int num)
    {
        char[] arr = num.ToString().ToCharArray();
        arr = arr.OrderByDescending(char.GetNumericValue).ToArray();
        var str = string.Join("", arr);

        return Convert.ToInt32(str);
    }
}
*/

using System.Linq;

public static class Kata
{
    public static int DescendingOrder(int num)
    {
        return int.Parse(string.Concat(num.ToString().OrderByDescending(c => c)));
    }
}