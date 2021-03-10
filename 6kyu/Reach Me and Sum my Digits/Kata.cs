using System.Linq;

public class SumDigNth
{
    public static long SumDigNthTerm(long initval, long[] patternl, int nthterm)
    {
        var cycleSum = Enumerable.Range(0, nthterm - 1).Sum(i => patternl[i % patternl.Length]);

        return (long) (initval + cycleSum).ToString().Sum(char.GetNumericValue);
    }
}