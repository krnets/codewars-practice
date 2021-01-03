using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static int FindMissing(List<int> list)
    {
        // int step = (list[^1] - list[0]) / list.Count;
        int step = (list.Last() - list.First()) / list.Count;

        for (int i = 0; i < list.Count - 1; i++)
            if (list[i + 1] - list[i] != step)
                return list[i] + step;

        return -1;
    }
}