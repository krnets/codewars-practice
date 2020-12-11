/*public class NthSeries
{
    public static string seriesSum(int n)
    {
        double sum = 0;

        for (int i = 0; i < n; i++)
            sum += 1.0 / (3 * i + 1);

        return sum.ToString("F");
    }
}*/

/*using System.Linq;

public class NthSeries
{
    public static string seriesSum(int n)
    {
        return Enumerable.Range(0, n).Aggregate(0.0, (acc, i) => acc + 1.0 / (3 * i + 1)).ToString("F");
    }
}*/

using static System.Linq.Enumerable;

public class NthSeries
{
    public static string seriesSum(int n)
    {
        return $"{Range(0, n).Sum(i => 1d / (3 * i + 1)):F}";
    }
}