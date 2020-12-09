using System.Linq;

public class Kata
{
    public static int PositiveSum(int[] arr) => arr.Where(x => x > 0).Sum();
}