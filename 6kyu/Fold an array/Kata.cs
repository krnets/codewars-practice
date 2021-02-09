/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static int[] FoldArray(int[] array, int runs)
    {
        var list = new List<int>(array);

        for (int i = 0; i < runs; i++)
        {
            for (int k = 0; k < (list.Count / 2); k++)
                list[k] += list[list.Count - k - 1];

            list = list.SkipLast(list.Count / 2).ToList();
        }

        return list.ToArray();
    }
}*/

/*using System.Linq;

public class Kata
{
    public static int[] FoldArray(int[] array, int runs)
    {
        int halfLength = array.Length / 2;

        var folded = array.Take(halfLength)
            .Zip(array.Reverse().Take(halfLength),
                (a, b) => a + b);

        if (array.Length % 2 == 1)
            folded = folded.Concat(new[] {array[halfLength]});

        runs--;

        return runs == 0 ? folded.ToArray() : FoldArray(folded.ToArray(), runs);
    }
}*/

using System.Linq;

public class Kata
{
    public static int[] FoldArray(int[] array, int runs)
    {
        if (runs == 0)
            return array;

        return FoldArray(Enumerable.Range(0, array.Length / 2)
            .Select(i => array[i] + array[array.Length - i - 1])
            .Concat((array.Length % 2 == 0) ? new int[] { } : new[] {array[array.Length / 2]})
            .ToArray(), runs - 1);
    }
}