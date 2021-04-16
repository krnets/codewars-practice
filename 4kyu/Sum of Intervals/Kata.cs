/*
using System.Collections.Generic;
using System.Linq;

public class Intervals
{
    public static int SumIntervals((int, int)[] intervals)
    {
        var set = new HashSet<int>();

        foreach ((int start, int end) in intervals)
            set.UnionWith(Enumerable.Range(start, end - start));

        var nums = set.OrderBy(x => x).ToArray();
        int sum = 0;

        for (int i = 0; i < nums.Length; i++)
        {
            var seq = new List<int> {nums[i]};

            while ((i < nums.Length - 1) && (nums[i + 1] == nums[i] + 1))
                seq.Add(nums[++i]);

            sum += seq.Last() - seq.First() + 1;
        }

        return sum;
    }
}
*/

/*
using System.Collections.Generic;
using System.Linq;

public class Intervals
{
    public static int SumIntervals((int, int)[] intervals)
    {
        var set = new HashSet<int>();

        foreach (var (start, end) in intervals)
            for (int i = start; i < end; i++)
                set.Add(i);

        return set.Count();
    }
}
*/

/*
using System.Linq;

public class Intervals
{
    public static int SumIntervals((int, int)[] intervals)
    {
        return intervals
            .SelectMany(i => Enumerable.Range(i.Item1, i.Item2 - i.Item1))
            .Distinct()
            .Count();
    }
}
*/

using System;
using System.Linq;

public class Intervals
{
    public static int SumIntervals((int, int )[] intervals)
    {
        if (intervals == null || intervals.Length == 0)
            return 0;

        var ordered = from interval in intervals orderby interval.Item1 select interval;

        int sum = 0, prevHigh = int.MinValue;

        foreach (var (low, high) in ordered)
            if (prevHigh < high)
            {
                sum += high - Math.Max(prevHigh, low);
                prevHigh = high;
            }

        return sum;
    }
}


/*using System;
using System.Linq;

public class Intervals
{
    public static int SumIntervals((int low, int high)[] intervals)
    {
        int prevHigh = int.MinValue;

        return intervals.OrderBy(tup => tup.low)
            .Aggregate(0, (acc, tup) => acc + (prevHigh < tup.high ? -Math.Max(tup.low, prevHigh) + (prevHigh = tup.high) : 0));
    }
}*/