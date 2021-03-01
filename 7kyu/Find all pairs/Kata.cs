using System.Linq;

class Kata
{
    public static int Duplicates(int[] a)
    {
        // return a.GroupBy(x => x).Select(g => g.Count() / 2).Sum();
        return a.GroupBy(x => x).Sum(g => g.Count() / 2);
    }
}