using System;
using NUnit.Framework;

[TestFixture]
public static class SumDigNthTests
{
    private static void testing(long actual, long expected)
    {
        Assert.AreEqual(expected, actual);
    }

    [Test]
    public static void Test1()
    {
        testing(SumDigNth.SumDigNthTerm(10, new long[] {2, 1, 3}, 6), 10);
    }

    [Test]
    public static void Test2()
    {
        testing(SumDigNth.SumDigNthTerm(10, new long[] {2, 1, 3}, 15), 10);
    }

    [Test]
    public static void Test3()
    {
        testing(SumDigNth.SumDigNthTerm(10, new long[] {2, 1, 3}, 50), 9);
    }

    [Test]
    public static void Test4()
    {
        testing(SumDigNth.SumDigNthTerm(10, new long[] {2, 1, 3}, 78), 10);
    }

    [Test]
    public static void Test5()
    {
        testing(SumDigNth.SumDigNthTerm(10, new long[] {2, 1, 3}, 157), 7);
    }
}