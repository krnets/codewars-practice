using System.Linq;

class Kata
{
    public static int MaxTriSum(int[] a)
    {
        return a.Distinct().OrderBy(x => x).TakeLast(3).Sum();
    }
}