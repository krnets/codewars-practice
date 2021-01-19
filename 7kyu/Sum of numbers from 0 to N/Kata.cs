/*using System.Linq;

public class SequenceSum
{
    public static string ShowSequence(int n)
    {
        if (n < 0) return $"{n}<0";
        if (n == 0) return "0=0";
        var nums = Enumerable.Range(0, n + 1).ToArray();

        return $"{string.Join('+', nums)} = {nums.Sum()}";
    }
}*/

using static System.Linq.Enumerable;

public class SequenceSum
{
    public static string ShowSequence(int n)
    {
        return (n == 0) ? "0=0" : (n < 0) ? $"{n}<0" :
            $"{string.Join('+', Range(0, n + 1))} = {(n + 1) * n / 2}";
    }
}