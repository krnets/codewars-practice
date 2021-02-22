using System.Linq;

public class Kata
{
    public static int LargestPairSum(int[] numbers)
    {
        return numbers.OrderBy(x => x).TakeLast(2).Sum();
    }
}