using System.Collections.Generic;
using System.Linq;

public static class SumOfK
{
    public static int? chooseBestSum(int t, int k, List<int> ls)
    {
        var distances = ls.Where(d => d <= t).ToList();

        return distances.Select((d, i) => d + (
                k > 1
                    ? chooseBestSum(t - d, k - 1, distances.Skip(i + 1).ToList())
                    : 0))
            .Max();
    }
}