/*using System.Linq;

public class Kata
{
    public static int HighestRank(int[] arr)
    {
        var dictionary = arr.GroupBy(x => x)
            .ToDictionary(g => g.Key, g => g.Count());

        var mostFrequent = dictionary.Values.Max();

        return dictionary.Where(kvp => kvp.Value == mostFrequent).Max(kvp => kvp.Key);
    }
}*/

using System.Linq;

public class Kata
{
    public static int HighestRank(int[] arr)
    {
        return arr.GroupBy(x => x).Max(g => (g.Count(), g.Key)).Key;
    }
}