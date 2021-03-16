/*using System;
using System.Linq;

public class Kata
{
    public static int[] TakeWhile(int[] arr, Func<int, bool> pred)
    {
        return arr.TakeWhile(pred).ToArray();
    }
}*/

/*using System;
using System.Collections.Generic;

public class Kata
{
    public static int[] TakeWhile(int[] arr, Func<int, bool> pred)
    {
        var result = new List<int>();

        foreach (int x in arr)
            if (pred(x))
                result.Add(x);
            else break;

        return result.ToArray();
    }
}*/

/*using System;

public class Kata
{
    public static int[] TakeWhile(int[] arr, Func<int, bool> pred)
    {
        for (int i = 0; i < arr.Length; i++)
            if (!pred(arr[i]))
            {
                Array.Resize(ref arr, i);
                break;
            }

        return arr;
    }
}*/

using System;

public class Kata
{
    public static int[] TakeWhile(int[] arr, Func<int, bool> pred)
    {
        int i = 0;

        foreach (int x in arr)
            if (pred(x)) i++;
            else break;

        var destinationArray = new int[i];
        Array.Copy(arr, destinationArray, i);

        return destinationArray;
    }
}