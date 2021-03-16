using System;

public class Kata
{
    public static int[] DropWhile(int[] arr, Func<int, bool> pred)
    {
        int i = 0;

        foreach (int x in arr)
            if (pred(x)) i++;
            else break;

        int n = arr.Length - i;
        var destinationArray = new int[n];
        Array.Copy(arr[i..], destinationArray, n);

        return destinationArray;
    }
}

/*using System;
using System.Linq;

public class Kata
{
    public static int[] DropWhile(int[] arr, Func<int, bool> pred)
    {
        return arr.SkipWhile(pred).ToArray();
    }
}*/