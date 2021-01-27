/*using System;

public class Kata
{
    public static int FindDup(int[] arr)
    {
        Array.Sort(arr);

        for (int i = 1; i < arr.Length; i++)
            if (arr[i - 1] == arr[i])
                return arr[i];

        return -1;
    }
}*/

using System.Linq;

public class Kata
{
    public static int FindDup(int[] arr)
    {
        //return arr.Sum() - arr.Union(arr).Sum();
        //return arr.Sum() - arr.Distinct().Sum();
        return arr.GroupBy(x => x).Single(g => g.Count() > 1).Key;
    }
}