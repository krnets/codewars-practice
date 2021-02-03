using System.Linq;

class Kata
{
    public static int NthSmallest(int[] arr, int pos)
    {
        return arr.OrderBy(x => x).ElementAt(pos - 1);
    }
}