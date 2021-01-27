using System.Linq;

public class Kata
{
    public static int MaxProduct(int[] arr, int size)
    {
        return arr.OrderBy(x => x).TakeLast(size).Aggregate((a, b) => a * b);
    }
}