using System.Linq;

public class Kata
{
    public static int DifferenceOfSquares(int n)
    {
        var range = Enumerable.Range(1, n).ToArray();
        var sum = range.Sum();

        return sum * sum - range.Sum(i => i * i);
    }
}

/*public class Kata
{
    public static int DifferenceOfSquares(int n)
    {
        return n * (n + 1) * (3 * n * n - n - 2) / 12;
    }
}*/