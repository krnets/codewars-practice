using System.Linq;

public class Kata
{
    public static int MostFrequentItemCount(int[] collection)
    {
        return collection.Length == 0 ? 0 : collection.GroupBy(x => x).Max(g => g.Count());
        // return collection.GroupBy(x => x).Select(g => g.Count()).DefaultIfEmpty(0).Max();
    }
}