using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static List<int> Solve(List<int> arr)
    {
        var iterMax = arr.OrderByDescending(i => i).GetEnumerator();
        var iterMin = arr.OrderBy(i => i).GetEnumerator();
        var result = new List<int>();

        for (int i = 0; i < arr.Count; i++)
            if (i % 2 == 0)
            {
                iterMax.MoveNext();
                result.Add(iterMax.Current);
            }
            else
            {
                iterMin.MoveNext();
                result.Add(iterMin.Current);
            }

        return result;
    }
}