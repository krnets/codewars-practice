/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static string AnySimilarity(List<int> firstList, List<int> secondList, int n)
    {
        var result = new List<string>();

        for (int i = 0; i <= firstList.Count - n; i++)
        {
            var listToCheck = firstList.Skip(i).Take(n).ToList();

            for (int t = 0; t <= secondList.Count - n; t++)
            {
                var secondListRange = secondList.Skip(t).Take(n);

                if (listToCheck.SequenceEqual(secondListRange))
                    result.Add(string.Join(",", listToCheck));
            }
        }

        return string.Join(" | ", result.Distinct());
    }
}*/

using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static string AnySimilarity(List<int> firstList, List<int> secondList, int n)
    {
        var firstSubSeqs = GetSubsequenceStrings(firstList, n);
        var secondSubSeqs = GetSubsequenceStrings(secondList, n);

        return string.Join(" | ", firstSubSeqs.Intersect(secondSubSeqs));
    }

    private static IEnumerable<string> GetSubsequenceStrings(List<int> list, int n)
    {
        // return Enumerable.Range(0, list.Count - n + 1).Select(i => string.Join(",", list.GetRange(i, n)));
        return list.SkipLast(n - 1).Select((_, i) => string.Join(",", list.GetRange(i, n)));
    }
}