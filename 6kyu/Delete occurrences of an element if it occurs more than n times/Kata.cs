/*using System.Collections.Generic;

public class Kata
{
    public static int[] DeleteNth(int[] arr, int x)
    {
        var counter = new Dictionary<int, int>();
        var list = new List<int>();

        foreach (int e in arr)
        {
            int n = 0;

            if (counter.ContainsKey(e))
                n = counter[e]++;
            else
                counter[e] = 1;

            if (n < x)
                list.Add(e);
        }

        return list.ToArray();
    }
}*/

using System.Collections.Generic;

public class Kata
{
    public static int[] DeleteNth(int[] arr, int x)
    {
        var counter = new Dictionary<int, int>();
        var list = new List<int>();

        foreach (int e in arr)
        {
            if (counter.ContainsKey(e))
                counter[e]++;
            else counter[e] = 1;

            if (counter[e] <= x)
                list.Add(e);
        }

        return list.ToArray();
    }
}