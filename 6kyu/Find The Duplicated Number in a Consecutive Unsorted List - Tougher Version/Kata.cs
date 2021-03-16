/*using System.Linq;

public class Kata
{
    public static int FindDup(int[] arr)
    {
        return arr.Sum() - arr.Distinct().Sum();
    }
}*/

/*using System.Linq;

public class Kata
{
    public static int FindDup(int[] arr)
    {
        return arr.Sum() - (arr.Length - 1) * arr.Length / 2;
    }
}*/

using System.Collections.Generic;

public class Kata
{
    public static int FindDup(int[] arr)
    {
        var set = new HashSet<int>();

        foreach (var x in arr)
            if (!set.Add(x))
                return x;

        return -1;
    }
}