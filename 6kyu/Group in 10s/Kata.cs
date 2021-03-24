using System.Linq;

public class Kata
{
    public static int[][] GroupIn10s(int[] array)
    {
        if (array.Length == 0) return new int[0][];

        var result = new int[array.Max() / 10 + 1][];

        foreach (var g in array.OrderBy(x => x).GroupBy(x => x / 10))
            result[g.Key] = g.ToArray();

        return result;
    }
}