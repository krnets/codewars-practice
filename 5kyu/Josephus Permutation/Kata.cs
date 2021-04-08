using System.Collections.Generic;

public class Josephus
{
    public static List<object> JosephusPermutation(List<object> items, int k)
    {
        var list = new List<object>();
        int i = 0;

        while (items.Count > 0)
        {
            i = (i + k - 1) % items.Count;
            list.Add(items[i]);
            items.RemoveAt(i);
        }

        return list;
    }
}