/*using NUnit.Framework;
using Interval = System.ValueTuple<int, int>;

public class IntervalTest
{
    [Test]
    public void ShouldHandleEmptyIntervals()
    {
        Assert.AreEqual(0, Intervals.SumIntervals(new Interval[] { }));
        Assert.AreEqual(0, Intervals.SumIntervals(new Interval[] {(4, 4), (6, 6), (8, 8)}));
    }

    [Test]
    public void ShouldAddDisjoinedIntervals()
    {
        Assert.AreEqual(9, Intervals.SumIntervals(new Interval[] {(1, 2), (6, 10), (11, 15)}));
        Assert.AreEqual(11, Intervals.SumIntervals(new Interval[] {(4, 8), (9, 10), (15, 21)}));
        Assert.AreEqual(7, Intervals.SumIntervals(new Interval[] {(-1, 4), (-5, -3)}));
        Assert.AreEqual(78, Intervals.SumIntervals(new Interval[] {(-245, -218), (-194, -179), (-155, -119)}));
    }

    [Test]
    public void ShouldAddAdjacentIntervals()
    {
        Assert.AreEqual(54, Intervals.SumIntervals(new Interval[] {(1, 2), (2, 6), (6, 55)}));
        Assert.AreEqual(23, Intervals.SumIntervals(new Interval[] {(-2, -1), (-1, 0), (0, 21)}));
    }

    [Test]
    public void ShouldAddOverlappingIntervals()
    {
        Assert.AreEqual(7, Intervals.SumIntervals(new Interval[] {(1, 4), (7, 10), (3, 5)}));
        Assert.AreEqual(6, Intervals.SumIntervals(new Interval[] {(5, 8), (3, 6), (1, 2)}));
        Assert.AreEqual(19, Intervals.SumIntervals(new Interval[] {(1, 5), (10, 20), (1, 6), (16, 19), (5, 11)}));
    }

    [Test]
    public void ShouldHandleMixedIntervals()
    {
        Assert.AreEqual(13, Intervals.SumIntervals(new Interval[] {(2, 5), (-1, 2), (-40, -35), (6, 8)}));
        Assert.AreEqual(1234,
            Intervals.SumIntervals(new Interval[] {(-7, 8), (-2, 10), (5, 15), (2000, 3150), (-5400, -5338)}));
        Assert.AreEqual(158,
            Intervals.SumIntervals(new Interval[] {(-101, 24), (-35, 27), (27, 53), (-105, 20), (-36, 26)}));
    }
}*/


using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Linq;
using In = System.ValueTuple<int, int>;

public class IntervalTest
{
    private In[] Shuffle(In[] a)
    {
        List<In> list = new List<In>(a);
        Shuffle(list);
        return list.ToArray();
    }

    private static void Shuffle<T>(List<T> deck)
    {
        var rnd = new Random();
        for (int n = deck.Count - 1; n > 0; --n)
        {
            int k = rnd.Next(n + 1);
            T temp = deck[n];
            deck[n] = deck[k];
            deck[k] = temp;
        }
    }

    private int ShuffleAndSumIntervals(In[] arg)
    {
        return Intervals.SumIntervals(Shuffle(arg));
    }

    [Test]
    public void ShouldHandleEmptyIntervals()
    {
        Assert.AreEqual(0, Intervals.SumIntervals(new In[] { }));
        Assert.AreEqual(0, ShuffleAndSumIntervals(new In[] {(4, 4), (6, 6), (8, 8)}));
    }

    [Test]
    public void ShouldAddDisjoinedIntervals()
    {
        Assert.AreEqual(9, ShuffleAndSumIntervals(new In[] {(1, 2), (6, 10), (11, 15)}));
        Assert.AreEqual(11, ShuffleAndSumIntervals(new In[] {(4, 8), (9, 10), (15, 21)}));
        Assert.AreEqual(7, ShuffleAndSumIntervals(new In[] {(-1, 4), (-5, -3)}));
        Assert.AreEqual(78, ShuffleAndSumIntervals(new In[] {(-245, -218), (-194, -179), (-155, -119)}));
    }

    [Test]
    public void ShouldAddAdjacentIntervals()
    {
        Assert.AreEqual(54, ShuffleAndSumIntervals(new In[] {(1, 2), (2, 6), (6, 55)}));
        Assert.AreEqual(23, ShuffleAndSumIntervals(new In[] {(-2, -1), (-1, 0), (0, 21)}));
    }

    [Test]
    public void ShouldAddOverlappingIntervals()
    {
        Assert.AreEqual(7, ShuffleAndSumIntervals(new In[] {(1, 4), (7, 10), (3, 5)}));
        Assert.AreEqual(6, ShuffleAndSumIntervals(new In[] {(5, 8), (3, 6), (1, 2)}));
        Assert.AreEqual(19, ShuffleAndSumIntervals(new In[] {(1, 5), (10, 20), (1, 6), (16, 19), (5, 11)}));
    }

    [Test]
    public void ShouldHandleMixedIntervals()
    {
        Assert.AreEqual(13, ShuffleAndSumIntervals(new In[] {(2, 5), (-1, 2), (-40, -35), (6, 8)}));
        Assert.AreEqual(1234,
            ShuffleAndSumIntervals(new In[] {(-7, 8), (-2, 10), (5, 15), (2000, 3150), (-5400, -5338)}));
        Assert.AreEqual(158, ShuffleAndSumIntervals(new In[] {(-101, 24), (-35, 27), (27, 53), (-105, 20), (-36, 26)}));
    }
}