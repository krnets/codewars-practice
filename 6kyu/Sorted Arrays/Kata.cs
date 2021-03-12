using System.Linq;

public class Kata
{
    public static int NthSmallest(int[][] arr, int n)
    {
        return arr.SelectMany(x => x).OrderBy(x => x).ElementAt(n - 1);
    }
}