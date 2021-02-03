using System.Linq;

public class Kata
{
    public static int Sum(int[] integers)
    {
        return integers.Sum();
    }

    public static int CountChar(char[] chars, char charToCount)
    {
        return chars.Where((c => c == charToCount)).Count();
    }

    public static int[] CalculateSquares(int start, int end)
    {
        return Enumerable.Range(start, end - start + 1).Select(i => i * i).ToArray();
    }
}