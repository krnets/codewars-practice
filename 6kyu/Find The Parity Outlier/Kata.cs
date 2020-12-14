/*using System.Linq;

public class Kata
{
    public static int Find(int[] integers)
    {
        var odd = integers.Where(i => i % 2 != 0).ToArray();
        var even = integers.Where(i => i % 2 == 0).ToArray();

        return odd.Length == 1 ? odd[0] : even[0];
    }
}*/

using System.Linq;

public class Kata
{
    public static int Find(int[] integers)
    {
        int cmp = integers.Select(i => i % 2).Take(3).Sum() < 2 ? 1 : 0;

        return integers.First(i => i % 2 == cmp);
    }
}