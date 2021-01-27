/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static int[] MenFromBoys(int[] a)
    {
        var odd = new List<int>();
        var even = new List<int>();

        foreach (var x in a.Distinct())
        {
            if (x % 2 == 0) even.Add(x);
            else odd.Add(x);
        }

        return Enumerable.Concat(even.OrderBy(x => x), odd.OrderByDescending(x => x)).ToArray();
    }
}*/

using System.Linq;

public class Kata
{
    public static int[] MenFromBoys(int[] a)
    {
        var men = a.Distinct().Where(x => x % 2 == 0);
        var boys = a.Except(men);

        return men.OrderBy(x => x).Concat(boys.OrderByDescending(x => x)).ToArray();
    }
}