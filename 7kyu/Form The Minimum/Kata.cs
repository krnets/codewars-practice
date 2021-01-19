using System.Linq;

class Kata
{
    public static long MinValue(int[] a)
    {
        return long.Parse(string.Concat(a.Distinct().OrderBy(n => n)));
    }
}