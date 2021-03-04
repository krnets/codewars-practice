/*using System.Linq;

public class Kata
{
    public static int[] SortTwisted37(int[] array)
    {
        return array.Select(Swap37).OrderBy(x => x).Select(Swap37).ToArray();
    }

    private static int Swap37(int n)
    {
        return int.Parse(string.Concat(n.ToString().Select(c => c is '3' ? '7' : c is '7' ? '3' : c)));
    }
}*/

using System.Linq;

public class Kata
{
    public static int[] SortTwisted37(int[] array)
    {
        return array
            .OrderBy(x => int.Parse(string.Concat(x.ToString().Select(c => c is '3' ? '7' : c is '7' ? '3' : c))))
            .ToArray();
    }
}