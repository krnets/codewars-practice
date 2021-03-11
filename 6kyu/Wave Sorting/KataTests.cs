using NUnit.Framework;
using System;
using static Kata;
using System.Collections.Generic;
using System.Linq;

[TestFixture]
public class KataTests
{
    private static readonly Random R = new Random(DateTime.Now.Millisecond);

    [Test, Repeat(200)]
    public void TestRandom()
    {
        var arr = RandArray(R.Next(48) + 2).ToArray();
        var expected = arr.OrderBy(o => o).ToArray();

        WaveSort(arr);
        var actual = arr.OrderBy(o => o).ToArray();

        CollectionAssert.AreEqual(expected, actual);
    }

    public static IEnumerable<int> RandArray(int lent)
    {
        var i = 0;
        while (i++ < lent)
            yield return R.Next(50);
    }
}