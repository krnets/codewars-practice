using System.Linq;

public class Solution
{
    public static int convergence(int n)
    {
        int baseSeries = 1;
        int testSeries = n;
        int length = 0;

        while (baseSeries != testSeries)
        {
            testSeries = GetNext(testSeries);

            while (baseSeries < testSeries)
                baseSeries = GetNext(baseSeries);

            length++;
        }

        return length;
    }

    private static int GetNext(int n)
    {
        return n < 10
            ? n + n
            : n + $"{n}".Select(c => c - '0').Where(x => x > 0).Aggregate((a, b) => a * b);
    }
}