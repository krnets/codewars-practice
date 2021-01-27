/*using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static int[] digitize(int n)
    {
        var list = new LinkedList<int>();

        while (n > 0)
        {
            list.AddFirst(n % 10);
            n /= 10;
        }

        return list.Count == 0 ? new[] {0} : list.Select(i => i).ToArray();
    }
}*/

using System.Linq;

public static class Kata
{
    public static int[] digitize(int n)
    {
        return n.ToString().Select(c => (int) char.GetNumericValue(c)).ToArray();
    }
}