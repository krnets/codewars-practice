using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static List<int> Largest(int n, List<int> xs)
    {
        return xs.OrderBy(x => x).TakeLast(n).ToList();
    }
}