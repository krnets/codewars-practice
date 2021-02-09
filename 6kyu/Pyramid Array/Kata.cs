using System.Linq;
using static System.Linq.Enumerable;

public class Kata
{
    public static int[][] Pyramid(int n)
    {
        return Range(1, n).Select(i => Repeat(1, i).ToArray()).ToArray();
    }
}