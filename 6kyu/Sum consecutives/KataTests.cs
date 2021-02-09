using System;
using System.Collections.Generic;
using NUnit.Framework;

[TestFixture]
public static class ConsecutivesTests
{
    [Test]
    public static void Test1()
    {
        var i = new List<int> {1, 4, 4, 4, 0, 4, 3, 3, 1};
        var o = new List<int> {1, 12, 0, 4, 6, 1};
        Console.WriteLine("Input: {1,4,4,4,0,4,3,3,1}");
        Assert.AreEqual(o, Consecutives.SumConsecutives(i));
    }

    [Test]
    public static void Test2()
    {
        var i = new List<int> {-5, -5, 7, 7, 12, 0};
        var o = new List<int> {-10, 14, 12, 0};
        Console.WriteLine("Input: {-5,-5,7,7,12,0}");
        Assert.AreEqual(o, Consecutives.SumConsecutives(i));
    }
}