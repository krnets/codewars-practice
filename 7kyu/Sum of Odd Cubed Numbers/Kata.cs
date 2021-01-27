using System.Linq;

public class Kata
{
    public static int CubeOdd(int[] arr)
    {
        //return arr.Where(x => x % 2 != 0).Select(x => x * x * x).Sum();
        //return arr.Select(x => x * x * x).Where(x => x % 2 != 0).Sum();
        return arr.Sum(x => x % 2 == 0 ? 0 : x * x * x);
    }
}