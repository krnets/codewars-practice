using System.Linq;

public class Kata
{
    public static int[] ExtraPerfect(int n)
    {
        return Enumerable.Range(1, n).Where(i => i % 2 != 0).ToArray();
    }
}