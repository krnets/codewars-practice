public static class Kata
{
    public static int SequenceSum(int start, int end, int step)
    {
        int sum = 0;

        for (int i = start; i <= end; i += step)
            sum += i;

        return sum;
    }
}

/*
using System.Linq;

public static class Kata
{
    public static int SequenceSum(int start, int end, int step)
    {
        return start > end
            ? 0
            : Enumerable.Repeat(start, (end - start) / step + 1)
                .Select((x, i) => x + step * i)
                .Sum();
    }
}
*/

/*using System.Linq;

public static class Kata
{
    public static int SequenceSum(int start, int end, int step)
    {
        return start > end ? 0 : Enumerable.Range(start, end - start + 1).Where(i => (i - start) % step == 0).Sum();
    }
}*/