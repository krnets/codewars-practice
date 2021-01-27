using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public static int[] solve(int[] arr)
    {
        var map = arr.GroupBy(i => i).ToDictionary(g => g.Key, g => g.Count());
        var list = new List<int>();

        foreach (var i in arr)
            if (map[i] > 1)
                map[i]--;
            else list.Add(i);

        return list.ToArray();
    }
}