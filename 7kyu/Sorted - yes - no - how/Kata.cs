/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static string IsSortedAndHow(int[] array)
    {
        var list = new List<int>();

        for (int i = 1; i < array.Length; i++)
            list.Add(array[i] - array[i - 1]);

        return list.All(x => x >= 0) ? "yes, ascending" :
            list.All(x => x <= 0) ? "yes, descending" : "no";
    }
}*/

using System.Linq;

public class Kata
{
    public static string IsSortedAndHow(int[] array)
    {
        bool ascending = array.OrderBy(x => x).SequenceEqual(array);
        bool descending = array.OrderByDescending(x => x).SequenceEqual(array);

        return ascending ? "yes, ascending" : descending ? "yes, descending" : "no";
    }
}